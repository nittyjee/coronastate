# Process 1
# This is the first process in the workflow after data extraction.
# The locations.csv file is updated with the latest geocoding file that we have

import pandas as pd
import numpy as np
###### Names of files ##########
path = "/home/nittyjee/code/coronastate/data/"
#path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/"
locations_file_name = "locations.csv"
output_locations_file_name = "locations.csv"
missing_locations_file_name = "missing_locations_report.csv"
geocode_db_file_name = "geocode.csv"
all_csv = "all.csv"
all_located_csv = "all_locations.csv"
most_recent_data = "most_recent.csv"
farawaydate = 20250101
sources_input_file = "../input/sources.csv"
###### No changes below this line ##################################

#Locations file
input_file = pd.read_csv(path+locations_file_name)
keep_columns = ['num', 'placetype', 'adm0', 'adm1', 'adm2', 'adm3', 'indiv']
input_file = input_file[keep_columns]
input_file = input_file.fillna("")
input_file["lookup"] = input_file["adm3"] +" "+input_file["adm2"] +" "+input_file["adm1"]+" "+input_file["adm0"]
input_file["lookup"] = input_file["lookup"].str.strip()
#Read the geocoded database
geocoded_db = pd.read_csv(path+geocode_db_file_name)
geocoded_db['lookup'] = geocoded_db['lookup'].str.strip()
merged_df = input_file.merge(geocoded_db, on = "lookup", how="left")

print("Input file dimensions")
print(input_file.shape)
print("Geocode file dimensions")
print(geocoded_db.shape)
print("Output file dimensions")
print(merged_df.shape)
print("merged_df")
print(merged_df.head())


#export missing data
missing_data = merged_df[ pd.isnull(merged_df.lat)]
print("Missing data file dimensions")
print(missing_data.shape)
missing_data.to_csv(path+missing_locations_file_name, index = False)

keep_columns.append("lat")
keep_columns.append("lon")

#export the locations data
merged_df = merged_df[keep_columns]
merged_df = merged_df.fillna("")

print("merged_df - head")
print(merged_df.head())
print("merged_df - tail")
print(merged_df.tail())
merged_df.to_csv(path+output_locations_file_name, index = False)

# Now, processing all.csv
#Ignore bad lines where some of the columns are mismatched
all_df = pd.read_csv(path+all_csv, error_bad_lines=False)
all_df = all_df.fillna("")
all_df["lookup"] = all_df["adm3"] +" "+all_df["adm2"] +" "+all_df["adm1"]+" "+all_df["adm0"]
# print("Testing all.csv")
# print(all_df.head())
all_df["lookup"] = all_df["lookup"].str.strip()

# print(all_df.columns)
# print(all_df.shape)
all_df =all_df.drop(columns = ["lat","num","lon"])

#Only keep locations that exist in the geocode, otherwise, we don't want to have null lat/long
all_locations_df = all_df.merge(geocoded_db, on = "lookup", how="inner")

############ Code to add DayEnd record with 20250101
print("Count of all_locations before adding Day End Record")
print(all_locations_df.shape)
#Find the unique rows and copy them to a dataframe
all_locations_df = all_locations_df.sort_values(["DayStart"])
#Fix Brazil and some south american countries
all_locations_df["DayEnd"] = np.where(all_locations_df["DayEnd"]<all_locations_df["DayStart"], all_locations_df["DayStart"],all_locations_df["DayEnd"])

unique_rows = all_locations_df.copy().drop_duplicates(subset = "lookup",keep = 'last')

# Create generated summary of most recent data in columns below.
# Sort by last update date, or number of cases, or both - or sortable?
# Place name
# Adm level
# Last update date (most recent DayStart)
# Data source
# Case Numbers
# Confirmed
# Deaths
# Recovered
# Active
#
# In addition:
# Data source external link
# Data source internal link

# Add columns to most_recent.csv summary of:
# 2 columns for raw file links: internal and external.
# Date file was last updated (not the last start date)

sources = pd.read_csv(sources_input_file)
print("Sources")
print(sources.head())
internal_source_dict = {
       1:"data/all_locations.csv",
       2:"data/newjob/all.json",
       3:"data/rawdata/data/india-data"
}
external_source_dict = {
       1:"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/",
       2:"https://raw.githubusercontent.com/stevenliuyi/covid19/master/public/data/all.json",
       3: "https://api.covid19india.org/districts_daily.json"
}

recent_df = unique_rows.copy()
recent_df = recent_df[["placetype","adm0","adm1","adm2","adm3","DayStart","source","cases","deaths","recovered"]]
recent_df = recent_df.rename(columns = {"DayStart":"Recent DayStart"})
recent_df["internal source"] = recent_df["source"].map(internal_source_dict)
recent_df["external source"] = recent_df["source"].map(external_source_dict)
recent_df = recent_df.merge(sources, on = "adm0",how = "left")
recent_df.to_csv(path+most_recent_data, index = False)


#Change the value of those rows
#Replace day start with day end so that there are no overlaps in the new record.

unique_rows["ds"] = pd.to_datetime(unique_rows["DayEnd"], format='%Y%m%d').dt.date + pd.DateOffset(1)
unique_rows["DayStart"] = unique_rows["ds"].dt.strftime('%Y%m%d')
unique_rows["DayEnd"] = farawaydate
unique_rows = unique_rows.drop(columns=["ds"])
print(unique_rows.head())
#unique_rows.to_csv("../output/_unique.csv", index = False)
#append the unique rows back to all_locations_df
all_locations_df = all_locations_df.append(unique_rows, ignore_index=True)

all_locations_df = all_locations_df.sort_values(["lookup","DayEnd"])
print("Count of all_locations after adding Day End Record")
print(all_locations_df.shape)
all_locations_df = all_locations_df.drop(columns = ["lookup"])

#This is the prefered order of columns in the dataset
columns_order = ['lat', 'lon', 'cases', 'deaths', 'recovered', 'DayStart',
       'DayEnd', 'placetype', 'adm0', 'adm1', 'adm2', 'adm3', 'indiv',
       'source']
all_locations_df = all_locations_df[columns_order]

#rename adm2. It was missing from the original file
all_locations_df.columns = ['lat', 'lon', 'cases', 'deaths', 'recovered', 'DayStart',
       'DayEnd', 'placetype', 'adm0', 'adm1', 'adm2', 'adm3', 'indiv',
       'source']
all_locations_df.to_csv(path+all_located_csv, index = False)

print(all_locations_df.head())
print(all_locations_df.shape)
