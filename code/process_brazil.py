import urllib.request
import tarfile
import pandas as pd
import os
import numpy as np

#path = "/home/nittyjee/code/coronastate/data/"
input_path = "/home/nittyjee/code/coronastate/input/"
output_path = "/home/nittyjee/code/coronastate/data/"

# input_path = "/home/himabindu/PycharmProjects/mapbox-geocoding/input/"
# output_path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/"

input_file="HIST_PAINEL_COVIDBR_11jul2020.xlsx"

output_file= "brazil.csv"

locations_file_name = "locations.csv"

all_csv = "all.csv"

################# No changes below ################


def drop_y(df):
    # list comprehension of the cols that end with '_y'
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)



input_pdf = pd.read_excel(input_path + input_file,
                        usecols=["estado","municipio",	"data"	,
                                 "casosAcumulado",		"obitosAcumulado",
                                 	"Recuperadosnovos",	"emAcompanhamentoNovos"	])

print(input_pdf.shape)
input_pdf = input_pdf.rename(columns= {"estado":"adm1",
                                    "municipio":"adm2",
                                        "data":"date",
                                        "casosAcumulado":"cum_cases",
                                        "obitosAcumulado":"deaths",
                                        "Recuperadosnovos":"new_recovered"
                                        })

print(input_pdf.columns)
print("Memory usage")
print(input_pdf.info(verbose=False, memory_usage="deep"))

# Second, wrangle the data to find the start date and end date for each location
input_pdf = input_pdf[['adm1', 'adm2',  'date', "cum_cases"]]
input_pdf = input_pdf.drop_duplicates()
input_pdf = input_pdf.fillna("")
df_sort = input_pdf.sort_values(['adm1', 'adm2',  'date', "cum_cases"])
#cumulative sum is confirmed
df_sort["date"] = pd.to_datetime(df_sort["date"])
print(df_sort.head())
print(df_sort.dtypes)

df_start_date = df_sort.drop_duplicates(subset = ['adm1', 'adm2', "cum_cases"], keep="first").reset_index(drop=True)
df_start_date.rename(columns = {"date":"DayStart"}, inplace=True)
print(df_start_date.head())
print(df_start_date.shape)
df_end_date = df_sort.drop_duplicates(subset = [ 'adm1', 'adm2',"cum_cases"], keep="last").reset_index(drop=True)
df_end_date.rename(columns = {"date":"DayEnd"}, inplace=True)
df_start_date["DayStart_Before"] =  pd.to_datetime(df_start_date["DayStart"], format='%m/%d/%Y').dt.date + pd.DateOffset(-1)
df_start_date["DayStart_Before"] = df_start_date["DayStart_Before"].dt.strftime('%Y%m%d')
print(df_end_date.head())
print(df_end_date.shape)
df1 = df_start_date.merge(df_end_date, how = "inner", on = [ 'adm1', 'adm2',  "cum_cases"], suffixes=('', '_y'))
df1["DayStart"] = df1["DayStart"].dt.strftime('%Y%m%d')
df1["DayEnd"] = df1["DayEnd"].dt.strftime('%Y%m%d')
drop_y(df1)

print(df1.shape)


print(df1.columns)
print(df1.tail())
# del df_start_date
# del df_end_date

df1['B_shifted'] = df1.groupby(['adm1', 'adm2'])['DayStart_Before'].transform(lambda x:x.shift(-1))



df1['num'] = None
df1["deaths"]=""
df1["recovered"]=""
df1['placetype'] = "adm2"
df1["adm0"] = "Brazil"
df1["adm3"] = ""
df1["indiv"] = ""
df1["source"] = 5
df1["lat"]=""
df1['lon']=""
df1.rename(columns = { "cum_cases":"cases" }, inplace=True)
df1["DayEnd"] = np.where(df1.B_shifted.isnull(), df1["DayStart"], df1.B_shifted)
df1 = df1[["num","lat","lon","cases","deaths",
           "recovered","DayStart","DayEnd","placetype","adm0","adm1","adm2","adm3","indiv","source"]]

df1.to_csv(output_path+output_file, index = False)
#rewrite all.csv
# all_csv_df = pd.read_csv(path+all_csv,  error_bad_lines=False)
# print(all_csv_df.shape)
# all2 = all_csv_df.append(df1).reset_index(drop=True)
# print(all2.shape)
# all2["num"] = all2.index + 1
# all2.to_csv(path+all_csv)
#
#
# ########### Append the locations file
#
# _locations_df = df1[["num","placetype","adm0","adm1","adm2","adm3","indiv","lat","lon"]]
# print(_locations_df.shape)
# _locations_df = _locations_df.drop_duplicates()
# print("After removing duplicates - unique number of districts")
# print(_locations_df.shape)
# # india_locations_df.to_csv("../output/india_locations.csv", index=False)
#
# locations_file = pd.read_csv(path+locations_file_name)
# print(locations_file.shape)
# locations_2 = locations_file.append(_locations_df).reset_index(drop=True)
# print(locations_2.shape)
# locations_2["num"] = locations_2.index + 1
# locations_2.to_csv(path+locations_file_name, index=False)