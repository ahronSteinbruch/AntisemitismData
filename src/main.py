import pandas as pd

from df_exploration import DfExploration
from json_bulder import JsonBulder
from dataCleaner import DataCleaner

data_url = "./data/tweets_dataset.csv"
df = pd.read_csv(data_url)


df['char_count'] = df['Text'].str.len()
df = df.sort_values('char_count', ascending=False)

#creat a new column with the length of text words
df['Text'] = df['Text'].str.split(' ')
df['lengths'] = df['Text'].map(len)



df = DataCleaner(df).getData()
json_bulder = JsonBulder(df)



