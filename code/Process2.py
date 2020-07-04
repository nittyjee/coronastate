# This is the third process in the workflow. It will look at the missing_location_report.csv
# and update the geocode.csv database

from api_keys import *
import pandas as pd
import unicodedata
import sys
from mapbox import Geocoder


############functions used

def get_lat_long(geo, input_string):
    response = geo.forward(input_string)
    print(response)
    print(input_string)
    result = ""
    if (response.status_code == 200):
        collection = response.json()
        print(collection)
        if (collection["features"]!=[]):
            first = collection['features'][0]
            result = first["center"]
    print(result)
    return(result)

def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')
########## end of functions ###############

print(MAPBOX_ACCESS_TOKEN)

path = "/home/nittyjee/code/coronastate/data/"
#path = "/home/himabindu/PycharmProjects/mapbox-geocoding/data/"
missing_locations_file_name = "missing_locations_report.csv"
geocode_db_file_name = "geocode.csv"

################ No changes below this line #################

missing_data = pd.read_csv(path+missing_locations_file_name)

geocoder = Geocoder(access_token = MAPBOX_ACCESS_TOKEN)


if sys.hexversion >= 0x3000000:
    # On Python >= 3.0.0
    missing_data["lookup1"] = missing_data.apply(lambda row: remove_diacritic(row["lookup"]).decode(),axis=1)
else:
    # On Python < 3.0.0
    missing_data["lookup1"]= missing_data.apply(lambda row: remove_diacritic(unicode(row["lookup"], 'ISO-8859-1')), axis = 1)

missing_data["lat_long"]= missing_data.apply(lambda row: str(get_lat_long(geocoder, row["lookup1"])), axis = 1)

print(missing_data.head(10))
new_locations = missing_data[missing_data["lat_long"] != ""]
if (new_locations.empty == False):
    print("new locations that need to be updated")
    print(new_locations.head(10))

    new_locations["lat_long"]= new_locations["lat_long"].str.replace('[', '')
    new_locations["lat_long"]= new_locations["lat_long"].str.replace(']', '')
    new_locations[['lon','lat']] = new_locations.lat_long.str.split(",",expand=True)
    new_locations = new_locations[["lookup", "lon", "lat"]]
    print(new_locations.head())
#new_locations.to_csv("../output/test.csv", index = False)

    master_geocode = pd.read_csv(path+geocode_db_file_name)
    print(master_geocode.shape)
    master_geocode = master_geocode.append(new_locations)
    master_geocode = master_geocode.sort_values("lookup")
    master_geocode = master_geocode[["lookup", "lon","lat"]]
    master_geocode.to_csv(path+geocode_db_file_name, index = False)
    print(master_geocode.shape)