import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

##################### path

print(datetime.now())

path = '/home/nittyjee/code/coronastate/data/'
global_name = 'global_worldometer_covid_data.csv'
country_name = 'country_worldometer_covid_data.csv'

############################# user func

def to_float(x):
    
    x_strip = x.replace(",","").replace("+","")
    
    try:
        return float(x_strip)
    except:
        return None

############################# scrape table

url = 'https://www.worldometers.info/coronavirus/#countries'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

table = soup.find('table', id ='main_table_countries_today')
table_body =table.find('tbody') 

rows =table_body.find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)
    
############################# Process global data
world_columns = [
            'index',
        'Country',
        'Total Cases',
        'New Cases',
        'Total Deaths',
        'New Deaths',
        'Total Recovered',
        'New Recovered',
        'Active Cases',
        'Serious, Critical',
        'Tot Cases/1M pop',
        'Deaths/1M pop']

df_world = pd.DataFrame(data[7]).T\
        .rename(columns ={i:x for i,x in enumerate(world_columns)})\
        .loc[:,world_columns].set_index('index')

cols_num = [x for x in world_columns if (x != 'index') and (x!= 'Country')]
for col in cols_num:
    df_world[col] = df_world[col].apply(to_float)
    
# df_world.head()

############################# Process country data
country_columns = [
            'index',
            'Country',
        'Total Cases',
        'New Cases',
        'Total Deaths',
        'New Deaths',
        'Total Recovered',
        'New Recovered',
        'Active Cases',
        'Serious, Critical',
        'Tot Cases/1M pop',
        'Deaths/1M pop',
        'Total Tests',
        'Tests/1M pop',
        'Population']

df_country = pd.DataFrame(data[8:])\
            .rename(columns ={i:x for i,x in enumerate(country_columns)})\
            .loc[:,country_columns].set_index('index')

cols_num = [x for x in country_columns if (x != 'index') and (x!= 'Country')]
for col in cols_num:
    df_country[col] = df_country[col].apply(to_float)

df_country['Country'] = df_country.Country.str.encode('ascii',errors = 'replace').str.decode('ascii')
# df_country.head()

############################# Save


df_world.to_csv(path + global_name, index = False)
# print('ok')
df_country.to_csv(path + country_name, index = False)
print('ok')