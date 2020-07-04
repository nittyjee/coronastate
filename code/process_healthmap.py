import urllib.request
import tarfile
import pandas as pd
import os
import numpy as np

path = "/home/nittyjee/code/coronastate/data/"
#path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/"

thetarfile = "https://github.com/beoutbreakprepared/nCoV2019/blob/master/latest_data/latestdata.tar.gz?raw=true"
output_file= "healthmap.csv"

locations_file_name = "locations.csv"

all_csv = "all.csv"

################# No changes below ################


def drop_y(df):
    # list comprehension of the cols that end with '_y'
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)


ftpstream = urllib.request.urlopen(thetarfile)
thetarfile = tarfile.open(fileobj=ftpstream, mode="r|gz")
thetarfile.extractall(path)

input_pdf = pd.read_csv(path + "latestdata.csv", usecols=["city",  'province', 'country', 'date_confirmation','latitude', 'longitude', 'age','sex'])

os.remove(path + "latestdata.csv")
print(input_pdf.shape)
input_pdf = input_pdf[input_pdf["age"].notnull()]
input_pdf = input_pdf[input_pdf["sex"].notnull()]
input_pdf = input_pdf[input_pdf["city"].notnull()]
keep_cols = ["city",  'province', 'country', 'date_confirmation','latitude', 'longitude']

input_pdf = input_pdf[keep_cols]
print(input_pdf.info(verbose=False, memory_usage="deep"))

df = input_pdf.groupby(['city', 'province', 'country', 'latitude', 'longitude', 'date_confirmation']).size().reset_index(name='counts')
df = df.rename(columns = {"counts":"confirmed"})
new= df["date_confirmation"].str.split(".",n = 2, expand = True)
df["day"] = new[0]
df["month"] = new[1]
df["year"] = new[2]
df["date"] = df["year"]+df["month"] + df["day"]
#there might some errors in some confirmed date fields. Coerce them and remove them later
df['date'] = pd.to_numeric(df['date'], errors='coerce')
print("Before numeric conversion")
print(df.shape)
df = df.dropna(subset=['date'])
print("After numeric conversion")
print(df.shape)
df['date'] = df['date'].astype('int')

df = df[['city', 'province', 'country', 'latitude', 'longitude', 'date',"confirmed"]]
df = df.sort_values(['city', 'province', 'country', 'latitude', 'longitude', 'date'])
df['total_confirmed'] = df.groupby(['city', 'province', 'country', 'latitude', 'longitude'])['confirmed'].cumsum()
#df.to_csv("../output/_temp.csv", index = False)
print(df.columns)
print(df.head())
print(df.shape)


#Save some RAM
del input_pdf

# Second, wrangle the data to find the start date and end date for each location
df_sort = df.sort_values(["country", "province","city", 'latitude', 'longitude',"date"])
#cumulative sum is confirmed


df_start_date = df_sort.drop_duplicates(subset = ["country", "province","city", 'latitude', 'longitude',"total_confirmed"], keep="first").reset_index(drop=True)
df_start_date.rename(columns = {"date":"DayStart"}, inplace=True)
print(df_start_date.head())
print(df_sort.shape)
df_end_date = df_sort.drop_duplicates(subset = ["country", "province","city", "total_confirmed"], keep="last").reset_index(drop=True)
df_end_date.rename(columns = {"date":"DayEnd"}, inplace=True)
df_start_date["DayStart_Before"] =  pd.to_datetime(df_start_date["DayStart"], format='%Y%m%d').dt.date + pd.DateOffset(-1)
df_start_date["DayStart_Before"] = df_start_date["DayStart_Before"].dt.strftime('%Y%m%d')
print(df_end_date.head())
df1 = df_start_date.merge(df_end_date, how = "inner", on = ["country", "province","city", "total_confirmed"], suffixes=('', '_y'))
df1['B_shifted'] = df1.groupby(["country", "province","city"])['DayStart_Before'].transform(lambda x:x.shift(-1))

drop_y(df1)

print(df1.columns)

df1['num'] = None
df1["deaths"]=""
df1["recovered"]=""
df1['placetype'] = "adm3"
df1["adm2"] = ""
df1["indiv"] = ""
df1["source"] = 4
df1.rename(columns = {'latitude':"lat", 'longitude':"lon", 'country':"adm0",
                      'province':"adm1", "city":"adm3",  "total_confirmed":"cases"}, inplace=True)
df1["DayEnd"] = np.where(df1.B_shifted.isnull(), df1["DayEnd"], df1.B_shifted)
df1 = df1[["num","lat","lon","cases","deaths",
           "recovered","DayStart","DayEnd","placetype","adm0","adm1","adm2","adm3","indiv","source"]]

df1.to_csv(path+output_file, index = False)
#rewrite all.csv
all_csv_df = pd.read_csv(path+all_csv,  error_bad_lines=False)
print(all_csv_df.shape)
all2 = all_csv_df.append(df1).reset_index(drop=True)
print(all2.shape)
all2["num"] = all2.index + 1
all2.to_csv(path+all_csv)


########### Append the locations file

_locations_df = df1[["num","placetype","adm0","adm1","adm2","adm3","indiv","lat","lon"]]
print(_locations_df.shape)
_locations_df = _locations_df.drop_duplicates()
print("After removing duplicates - unique number of districts")
print(_locations_df.shape)
# india_locations_df.to_csv("../output/india_locations.csv", index=False)

locations_file = pd.read_csv(path+locations_file_name)
print(locations_file.shape)
locations_2 = locations_file.append(_locations_df).reset_index(drop=True)
print(locations_2.shape)
locations_2["num"] = locations_2.index + 1
locations_2.to_csv(path+locations_file_name, index=False)