import pandas as pd

key = '' #add key before running
url = 'https://api.census.gov/data/2019/acs/acs5/subject?get=NAME,GEO_ID,S1901_C01_012E,S1501_C02_015E,S1701_C03_001E&for=place:*&in=state:06&key=' + key
d = pd.read_json(url)
d.columns = d.iloc[0,:]
d = d[1:] #remove name row

d.to_csv('census_place.csv')

url2 = 'https://api.census.gov/data/2019/acs/acs5/subject?get=NAME,GEO_ID,S1901_C01_012E,S1501_C02_015E,S1701_C03_001E&for=county:*&in=state:06&key=' + key
c = pd.read_json(url2)
c.columns = c.iloc[0,:]
c = c[1:]

c.to_csv('census_county.csv')