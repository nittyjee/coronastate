# Scrape district data from covid19india website
# And rewrite all.csv

import pandas as pd
import requests

##### some user defined functions ##################
def flatten_dict(d):
    """ Returns list of lists from given dictionary """
    l = []
    for k, v in sorted(d.items()):
        if isinstance(v, dict):
            flatten_v = flatten_dict(v)
            for my_l in reversed(flatten_v):
                my_l.insert(0, k)

            l.extend(flatten_v)

        elif isinstance(v, list):
            for l_val in v:
                l.append([k, l_val])

        else:
            l.append([k, v])

    return l

def drop_y(df):
    # list comprehension of the cols that end with '_y'
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)

################# End of user defined functions

######### defintions of global variables ####################

path = "/home/nittyjee/code/coronastate/data/"
#path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/"

url = 'https://api.covid19india.org/districts_daily.json'

locations_file_name = "locations.csv"

all_csv = "all.csv"

################### end of global variables #####################Prakasam

# First, read the json file and convert to pandas dataframe
# Not using pandas' read_json because we need to flatten and normalize this json file
data = requests.get(url=url).json()
data = data["districtsDaily"]
df0 = pd.DataFrame(flatten_dict(data))
df0.columns = ["state","district","third_col"]
df1 = pd.io.json.json_normalize(df0['third_col'])
df0.drop(columns=["third_col"], inplace=True)
df = pd.concat([df0, df1], axis=1)
df["date"] = pd.to_datetime(df["date"], format='%Y-%m-%d')
df["date"]  = df["date"].dt.strftime('%Y%m%d')

keep_columns = ['state', 'district', 'active', 'confirmed', 'deceased', 'recovered', 'date']
df = df[keep_columns]
df.to_csv("../data/india_districts.csv", index=False)
# Second, wrangle the data to find the start date and end date for each district
df_sort = df.sort_values(["state", "district", "date"])
df_start_date = df_sort.drop_duplicates(subset = ["state", "district", "confirmed"], keep="first").reset_index(drop=True)
df_start_date.rename(columns = {"date":"DayStart"}, inplace=True)
print(df_start_date.head())
print(df_sort.shape)
df_end_date = df_sort.drop_duplicates(subset = ["state", "district", "confirmed"], keep="last").reset_index(drop=True)
df_end_date.rename(columns = {"date":"DayEnd"}, inplace=True)
print(df_end_date.head())
df1 = df_start_date.merge(df_end_date, how = "inner", on = ["state", "district", "confirmed"], suffixes=('', '_y'))
drop_y(df1)
# After looking at few things
#Hima Things to do
# We have to remove duplicate districts
# E.g. Y.S.R Kadapa, Y.S.R., Y.S.R. Kadapa


# Now, add variables that match with the locations.csv and all.csv

df1['num'] = None
df1['lat']=None
df1['lon']=None
df1['placetype'] = "adm2"
df1['adm0'] = "India"
df1["adm3"] = ""
df1["indiv"] = ""
df1["source"] = 3
df1.rename(columns = {"state":"adm1", "district":"adm2", "deceased":"deaths", "confirmed":"cases"}, inplace=True)

df1 = df1[["num","lat","lon","cases","deaths",
           "recovered","DayStart","DayEnd","placetype","adm0","adm1","adm2","adm3","indiv","source"]]

print(df1.shape)
df1.to_csv("../data/india_districts.csv", index=False)
all_csv_df = pd.read_csv(path+all_csv,  error_bad_lines=False)
print(all_csv_df.shape)
all2 = all_csv_df.append(df1).reset_index(drop=True)
print(all2.shape)
all2["num"] = all2.index + 1

all2.to_csv(path+all_csv)

########### Append the locations file

india_locations_df = df1[["num","placetype","adm0","adm1","adm2","adm3","indiv","lat","lon"]]
print(india_locations_df.shape)
india_locations_df = india_locations_df.drop_duplicates()
print("After removing duplicates - unique number of districts")
print(india_locations_df.shape)
# india_locations_df.to_csv("../output/india_locations.csv", index=False)

locations_file = pd.read_csv(path+locations_file_name)
print(locations_file.shape)
locations_2 = locations_file.append(india_locations_df).reset_index(drop=True)
print(locations_2.shape)
locations_2["num"] = locations_2.index + 1
locations_2.to_csv(path+locations_file_name, index=False)
