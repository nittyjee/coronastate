#Update geocoding.
#Trust geocoding to be better in datasource1, even better than mapbox

import pandas as pd
import numpy as np
path = "/home/nittyjee/code/coronastate/data/"
#path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/"
missing_locations_file_name = "missing_locations_report.csv"
original_geocode_db_file_name = "geocode.csv"

datasource1_filename = "datasource1.csv"

############### No changes below this line #######################

#Read datasource1. Remember that this file still has a few rows with extra columns.
# Ignoring those colums with error_bad_lines paraemter below
ds_file = pd.read_csv(path+datasource1_filename, error_bad_lines=False)
print(ds_file.columns)
keep_columns = ['lat','lon', 'placetype', 'adm0', 'adm1', 'adm2', 'adm3', 'indiv']
ds_file = ds_file[keep_columns]
print(ds_file.shape)
# Remove any duplicates to get lat/lon combinations
ds_file = ds_file.drop_duplicates()
print(ds_file.shape)
ds_file = ds_file.rename(columns = {"lat":"ds_lat", "lon":"ds_lon"})
ds_file = ds_file.fillna("")
ds_file["lookup"] = ds_file["adm3"] +" "+ds_file["adm2"] +" "+ds_file["adm1"]+" "+ds_file["adm0"]
ds_file["lookup"] = ds_file["lookup"].str.strip()
print(ds_file.columns)
#Read the geocoded database
geocoded_db = pd.read_csv(path+original_geocode_db_file_name)
geocoded_db['lookup'] = geocoded_db['lookup'].str.strip()
print(geocoded_db.columns)
print(geocoded_db.head())
merged_df = geocoded_db.merge(ds_file, on = "lookup", how="left")

#Replace lon and lat in geocoded database from data source 1
# If a location doesn't have lat/long from datasource 1, then use it from the geocoder
merged_df['lon'] = np.where(merged_df['ds_lon'].isna(), merged_df['lon'], merged_df['ds_lon'])
merged_df['lat'] = np.where(merged_df['ds_lat'].isna(), merged_df['lat'], merged_df['ds_lat'])

merged_df = merged_df[["lookup", "lat","lon"]]
print(merged_df.dtypes)
print(merged_df.shape)
print("After removing null values")
merged_df = merged_df[(merged_df.lat != 0) & (merged_df.lon != 0 ) ]
print(merged_df.shape)
merged_df = merged_df.drop_duplicates()
print(merged_df.shape)
#Replace the geocode database
merged_df.to_csv(path+original_geocode_db_file_name, index = False)
print(merged_df.head(10))