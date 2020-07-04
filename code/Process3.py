# This code adds a new column with the dataset name
import pandas as pd

def add_column(filename, datasetname):
    print("Processing "+filename)
    d = pd.read_csv(filename, error_bad_lines=False)
    d["data_set_name"] = datasetname
    d.to_csv(filename, index = False)

path = "/home/nittyjee/code/coronastate/data/"
# add_column(path+"all.csv", "all")
# add_column(path+"datasource1.csv", "datasource1")
# add_column(path+"datasource2.csv", "datasource2")
add_column(path+"locations.csv", "locations")
add_column(path+"all_locations.csv", "all_locations")
