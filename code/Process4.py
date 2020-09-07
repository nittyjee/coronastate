#This code splits all_locations into table for different layers in a map.
#The table details are as follows

# adm0
# adm1 tables:
# - adm1_bunch1: rest
# - adm1_bunch2:
#   * Equador
#   * Iran
#   * Ireland
#   * Switzerland
#   * Thailand
#   * South Korea
# adm2
# adm3

########### Any changes to the input and output files are made here ###########
input_path = "/home/nittyjee/code/coronastate/data/"
#input_path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/"
output_path = "/home/nittyjee/code/coronastate/data/layers/"
#output_path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/layers/"
all_located_csv = "all_locations.csv"
farawaydate = 20250101

############# No changes below this line #################

import pandas as pd
import numpy as np
import geopandas

# Step 1: Read the input file
all_locations = pd.read_csv(input_path+all_located_csv)
#Fill na values with blank
all_locations = all_locations.fillna("")

# Firstly, delete rows that have Mainland China in adm1 and no other city in any other location
all_locations["lookup"] = all_locations["adm3"] +" "+all_locations["adm2"] +" "+all_locations["adm1"]+" "+all_locations["adm0"]
all_locations["lookup"] = all_locations["lookup"].str.strip()
#number of original rows
print(all_locations.shape)
#remove the following locations
remove_location_list = ["Mainland China China", "Diamond Princess", "MS Zaandam", "West Bank and Gaza",
                        "Burma", "International Conveyance", "Diamond Princess International Conveyance",
                        "Metropolitan France France"]
for r in remove_location_list:
    all_locations = all_locations[all_locations["lookup"] != r]
    print("After removal of "+r)
    print(all_locations.shape)

#all_locations.to_csv("../output/debug.csv", index = False)
all_locations = all_locations.drop(columns = ["lookup"])

#delete duplicate USA from source 2
rowNames = all_locations[(all_locations['placetype'] =="adm0") & (all_locations['adm0'] == 'United States of America') & (all_locations['source'] == 2)].index
all_locations.drop(rowNames, inplace=True)
print("After removing USA from source 2")
print(all_locations.shape)
#Traverse through each row of the table and remove mainland china and move up all the other locations (adm2 through adm3)
#Note that adm3 will be blank
for i, row in all_locations.iterrows():
    if (row["adm1"]=="Mainland China"):

        all_locations.at[i,'adm1'] =row["adm2"]
        all_locations.at[i, 'adm2'] = row["adm3"]
        all_locations.at[i, 'adm3'] = ""
        #Updates the placetype because we shifted by 1 after deleting Mainland China
        if (row["placetype"] == "adm3"):
            all_locations.at[i, 'placetype'] = "adm2"
        elif (row["placetype"] == "adm2"):
            all_locations.at[i, 'placetype'] = "adm1"
        elif (row["placetype"] == "adm1"):
            all_locations.at[i, 'placetype'] = "adm0"
#Remove duplicates and keep only source 1



#Verify the total number of placetypes
print(all_locations["placetype"].value_counts())
adm0_df = all_locations[all_locations["placetype"] == "adm0"]
adm2_df = all_locations[all_locations["placetype"] == "adm2"]
adm3_df = all_locations[all_locations["placetype"] == "adm3"]
adm1_df = all_locations[all_locations["placetype"] == "adm1"]
#adding healthmap separarte dataset
adm3_healthmap_df = adm3_df.copy()
adm3_healthmap_df = adm3_healthmap_df[adm3_healthmap_df["source"]==4]


#Verify that the number of rows for adm0 through adm3 add up to the total
print(all_locations.shape)
#delete the dataframe to save some space
del all_locations
print(adm0_df.shape)
print(adm1_df.shape)
print(adm2_df.shape)
print(adm3_df.shape)

# Now split adm1 into two different tables
print(adm1_df["adm1"].value_counts())
mylist = ["Ecuador","Iran","Ireland","Switzerland", "Thailand","South Korea"]

#bunch2 that contains the above countries
adm1_df_bunch2 = adm1_df.copy()[adm1_df["adm0"].isin(mylist)]
print(adm1_df_bunch2.shape)

#bunch1 that does not contain the aboce countries
adm1_df_bunch1 = adm1_df.copy()[~adm1_df["adm0"].isin(mylist)]
print(adm1_df_bunch1.shape)

#Removing duplicates for source 2 in China
adm1_df_bunch1["lookup"] = adm1_df_bunch1["adm3"] +" "+adm1_df_bunch1["adm2"] +" "+adm1_df_bunch1["adm1"]+" "+adm1_df_bunch1["adm0"]
adm1_df_bunch1["lookup"] = adm1_df_bunch1["lookup"].str.strip()

print("Before removing China Duplicates")
print(adm1_df_bunch1.shape)

#identify lookups that have duplicates
# by counting the number of sources each lookup has.
# if a lookup has 2 sources, then they need to be deleted because it is a duplicate
dup_count = adm1_df_bunch1.groupby(["lookup"], as_index=False).agg({'source': 'nunique'})
dup_count = dup_count[dup_count.source == 2]
dup_count["dummy"] = "del"
adm1_df_bunch1_v1 = adm1_df_bunch1.merge(dup_count, on = ["lookup","source"], how = "left")
adm1_df_bunch1_v1 = adm1_df_bunch1_v1[adm1_df_bunch1_v1.dummy.isnull()]
adm1_df_bunch1 = adm1_df_bunch1_v1.drop(columns = ["lookup", "dummy"])


print("After removing China Duplicates")
print(adm1_df_bunch1.shape)

# Merging: adm1_bunch1 and adm1_bunch2
# Reducing to a single row for each adm1 place of the last DayStart row.
# Where DayStart is longer than 2 weeks before the current date, limit it to 2 weeks, so all the circles will disappear by 2 weeks before the current date.
adm1_static = pd.concat([adm1_df_bunch1, adm1_df_bunch2], ignore_index=True)

def create_static_dataset(input_df):
    _static = input_df.copy()
    _static["new_date"] = pd.to_datetime(_static["DayStart"], format='%Y%m%d')
    _static['date_cutoff'] = pd.to_datetime("now") - pd.DateOffset(days=14)
    _static['yesterday'] = pd.to_datetime("now") - pd.DateOffset(days=1)
    _static['diff_days'] = pd.to_datetime("now") - _static["new_date"]
    _static['today'] = pd.to_datetime("now")
    _static["lookup"] = _static["adm3"] + " " + _static["adm2"] + " " + _static["adm1"] + " " + \
                            _static["adm0"]
    _static["lookup"] = _static["lookup"].str.strip()
    _static = _static.sort_values('DayStart', ascending=False)
    _static = _static.drop_duplicates(subset='lookup', keep='first')
    _static = _static.drop(columns=["lookup"])
    _static["new_date"] = np.where(_static["new_date"] < _static['date_cutoff'], _static['date_cutoff'],
                                       _static["new_date"])
    # Checking if new_date is greater than current date. If so, we should change it to current date. This only happens for static file
    _static["new_date"] = np.where(_static["new_date"] > _static['yesterday'], _static['yesterday'],
                                       _static["new_date"])

    _static["new_date_str"] = _static["new_date"].dt.strftime('%Y%m%d')
    _static["DayStart"] = _static["new_date_str"].astype(int)
    _static = _static[["lat", "lon", "cases", "deaths", "recovered", "DayStart", "DayEnd",
                               "placetype", "adm0", "adm1", "adm2", "adm3", "indiv", "source"]]
    return(_static)

adm1_static = create_static_dataset(adm1_static.copy())
adm2_static = create_static_dataset(adm2_df)
adm3_static = create_static_dataset(adm3_df)
adm3_healthmap_static = create_static_dataset(adm3_healthmap_df)


def convert_to_geojson(input_df, output_file):
    gdf = geopandas.GeoDataFrame(
        input_df, geometry=geopandas.points_from_xy(input_df.lon, input_df.lat))
    gdf.to_file(output_path+output_file, driver='GeoJSON')

#output geojson files for tileset
convert_to_geojson(adm0_df, "adm0.geojson")
convert_to_geojson(adm1_df_bunch1, "adm1_bunch1.geojson")
convert_to_geojson(adm1_df_bunch2, "adm1_bunch2.geojson")
convert_to_geojson(adm2_df, "adm2.geojson")
convert_to_geojson(adm3_df, "adm3.geojson")
convert_to_geojson(adm3_healthmap_df, "adm3_healthmap.geojson")
convert_to_geojson(adm1_static, "static_adm1.geojson")
convert_to_geojson(adm2_static, "static_adm2.geojson")
convert_to_geojson(adm3_static, "static_adm3.geojson")
convert_to_geojson(adm3_healthmap_static, "static_adm3_healthmap.geojson")

#Finally export the tables as csvs
adm0_df.to_csv(output_path+"adm0.csv", index =False)
adm1_df_bunch1.to_csv(output_path+"adm_bunch1.csv", index =False)
adm1_df_bunch2.to_csv(output_path+"adm_bunch2.csv", index =False)
adm2_df.to_csv(output_path+"adm2.csv", index =False)
adm3_df.to_csv(output_path+"adm3.csv", index =False)
adm3_healthmap_df.to_csv(output_path+"adm3_healthmap.csv", index =False)
adm1_static.to_csv(output_path+"static_adm1.csv", index =False)
adm2_static.to_csv(output_path+"static_adm2.csv", index = False)
adm3_static.to_csv(output_path+"static_adm3.csv", index = False)
adm3_healthmap_static.to_csv(output_path+"static_adm3_healthmap.csv", index = False)
