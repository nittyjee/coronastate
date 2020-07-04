import pandas as pd
import requests
import json
import numpy as np

##### some user defined functions ##################

def flatten_dict(d):
    """ Returns list of lists from given dictionary """
    l = []
    for k, v in d.items():
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


def process_json_df(df_temp):
    # the input parameter is a pandas dataframe with some rows containing "ENGLISH"
    # followed by confirmed, deaths, and cured by dates

    #initialize empty list
    # These are the columns
    adm0_list = []
    adm1_list = []
    adm2_list = []
    adm3_list = []
    variable_list = []
    date_list = []
    value_list = []

    # The following is a running tally to track which country/state/district/city we are tracking
    current_adm0 = ""
    current_adm1 = ""
    current_adm2 = ""
    current_adm3 = ""
    #The following variable will track where either confirmed, recovered, or death variable starts

    current_variable_column = 0
    i = 0
    j = i + 1
    k = j + 1
    l = k + 1
    for index, row in df_temp.iterrows():
        if (row[i] == "ENGLISH"):
            delete_flag = 0
            if (row[i+1] == ""):
                delete_flag = 1
            current_adm0 = row[i+1]
            current_adm1 = ""
            current_adm2 = ""
            current_adm3 = ""
            current_variable_column = i
        elif (row[j] == "ENGLISH"):
            delete_flag = 0
            if (row[j + 1] == ""):
                delete_flag = 1
            current_adm1 = row[j+1]
            current_adm2 = ""
            current_adm3 = ""
            current_variable_column = j
        elif (row[k] == "ENGLISH"):
            delete_flag = 0
            if (row[k+1] == ""):
                delete_flag = 1
            current_adm2 = row[k+1]
            current_adm3 = ""
            current_variable_column = k
        elif (row[l] == "ENGLISH"):
            delete_flag = 0
            if (row[l+1] == ""):
                delete_flag = 1
            current_adm3 = row[l+1]
            current_variable_column = l
        else:
            if (delete_flag == 0):
                var = row[current_variable_column]
                date = row[current_variable_column + 1]
                value = row[current_variable_column + 2]
                adm0_list.append(current_adm0)
                adm1_list.append(current_adm1)
                adm2_list.append(current_adm2)
                adm3_list.append(current_adm3)
                variable_list.append(var)
                date_list.append(date)
                value_list.append(value)

    new_df = pd.DataFrame({"adm0": adm0_list, "adm1": adm1_list, "adm2": adm2_list, "adm3": adm3_list,
                           "var_type": variable_list, "date": date_list, "value": value_list})
    print(new_df.shape)
    return(new_df)


################# End of user defined functions

base_source_path = "../covid19/data/data"
base_dest_path = "../raw_data"
base_source_path = "/home/nittyjee/code/covid19/data"
base_dest_path = "/home/nittyjee/code/coronastate/data/rawdata/data"



################### end of global variables #####################Prakasam
f = base_source_path + "/1p3a-data/confirmed.json"
with open(f) as json_file:
    data = json.load(json_file)
df0 = pd.DataFrame(data)
#print(df0.head())
print(df0.columns)
print(df0.shape)
o = base_dest_path + "/1p3a-data/confirmed.csv"
df0.to_csv(o, index=False)

f = base_source_path + "/1p3a-data/deaths.json"
with open(f) as json_file:
    data = json.load(json_file)
df0 = pd.DataFrame(data)
#print(df0.head())
print(df0.columns)
print(df0.shape)
o = base_dest_path + "/1p3a-data/deaths.csv"
df0.to_csv(o, index=False)

f = base_source_path + "/hong-kong-data/raw.json"
with open(f) as json_file:
    data = json.load(json_file)
df0 = pd.DataFrame(data)
#print(df0.head())
print(df0.columns)
print(df0.shape)
o = base_dest_path + "/hong-kong-data/raw.csv"
df0.to_csv(o,  encoding = 'utf-8', index=False)


f = base_source_path + "/saudi-arabia-data/raw.json"
with open(f) as json_file:
    data = json.load(json_file)
df0 = pd.DataFrame(data)
#print(df0.head())
print(df0.columns)
print(df0.shape)
o = base_dest_path + "/saudi-arabia-data/raw.csv"
df0.to_csv(o, index=False)

f = base_source_path + "/thailand-data/raw.json"
with open(f) as json_file:
    data = json.load(json_file)
df0 = pd.DataFrame(data)
print(df0.head())
print(df0.columns)
print(df0.shape)
o = base_dest_path + "/thailand-data/raw.csv"
df0.to_csv(o, index=False)

f = base_source_path + "/india-data/raw.json"
with open(f) as json_file:
    data = json.load(json_file)
print(data)
df0 = pd.DataFrame(data)
print(df0.head())
print(df0.columns)
print(df0.shape)
o = base_dest_path + "/india-data/raw.csv"
df0.to_csv(o, index=False)
