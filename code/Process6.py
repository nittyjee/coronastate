#Creates summary tables for the graphs and tables

import datetime as dt
import pandas as pd


input_path = "/home/nittyjee/code/coronastate/data/layers/"
#input_path = "/home/admin-home/PythonProjects/upwork-mapboxgeocoding/data/layers/"

overall_summary_csv = "../data/overall_summary.csv"
country_summary_csv = "../data/country_summary.csv"
###################### No changes below ######################


adm0 = pd.read_csv(input_path+"adm0.csv")
adm0["DayStart"] = pd.to_datetime(adm0["DayStart"], format='%Y%m%d')
adm0["DayEnd"] = pd.to_datetime(adm0["DayEnd"], format='%Y%m%d')
keep_columns = ['cases', 'deaths', 'recovered', 'DayStart', 'DayEnd','adm0']
adm0 = adm0[keep_columns]
#Starting at 1/25/2020
date_array = pd.date_range(start = dt.datetime(2020,1,25), end = dt.datetime.now())
print(adm0.dtypes)
pdf = pd.DataFrame()

for i in date_array:
    temp = adm0.copy()
    i = i.to_pydatetime()
    mask = (temp['DayStart'] <= i) & (i <= temp['DayEnd'] )
    temp = temp[mask]
    temp = temp[["cases","deaths","recovered","adm0"]]
    temp["date"] = i

    pdf = pdf.append(temp, ignore_index = True)
#pdf.to_csv("../output/_temp.csv")
pdf2 = pdf.groupby("date").agg({"cases":"sum", "deaths":"sum", "recovered":"sum"})
pdf2["deaths"] = pdf2["deaths"].astype(int)
pdf2["recovered"] = pdf2["recovered"].astype(int)
pdf2["active"] = pdf2["cases"] - pdf2["recovered"]
pdf2['cases_prev'] = pdf2['cases'].shift(1)
pdf2['daily_cases'] = pdf2['cases'] - pdf2['cases_prev']
print(pdf2.head())
pdf2['roll_cases'] = pdf2["daily_cases"].rolling(window=7).mean()
pdf2['roll_cases_prev'] = pdf2['roll_cases'].shift(1)
pdf2["case_rate"]  = pdf2['roll_cases']/pdf2['roll_cases_prev'] - 1
pdf2 = pdf2.drop(columns=['roll_cases','roll_cases_prev', "cases_prev"] )
pdf2.to_csv(overall_summary_csv)
print(pdf.columns)
pdf3 = pdf.groupby(["date","adm0"]).agg({"cases":"sum", "recovered":"sum", "deaths":"sum"})
pdf3 = pd.DataFrame(pdf3).reset_index()
pdf3["deaths"] = pdf3["deaths"].astype(int)
pdf3["recovered"] = pdf3["recovered"].astype(int)

pdf3 = pdf3.rename(columns={"date":"Date",
                            "adm0":"Country",
                            "cases":"Confirmed",
                            "recovered":"Recovered",
                            "deaths":"Deaths"})
pdf3 = pdf3.sort_values(["Country", "Date"]).reset_index(drop=True)

pdf3['cases_prev'] = pdf3.groupby(['Country'])['Confirmed'].shift(1)
print(pdf3.head(10))
pdf3['daily_cases'] = pdf3["Confirmed"] - pdf3['cases_prev']
pdf3['moving'] = pdf3.groupby(['Country']).rolling(7)['daily_cases'].mean().reset_index(drop=True)
pdf3['prev_value'] = pdf3.groupby(['Country'])['moving'].shift(1)
pdf3['cases_rate'] = pdf3['moving']/pdf3['prev_value'] - 1
pdf3 = pdf3.drop(columns=["prev_value", "cases_prev"])
# pdf3 = pdf3.sort_values(["Date","Country"])
print(pdf3.head(10))
pdf3.to_csv(country_summary_csv)
