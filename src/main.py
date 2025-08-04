from pprint import pprint

import pandas as pd
import numpy as np

from df_exploration import DfExploration
from json_bulder import JsonBulder
from dataCleaner import DataCleaner

data_url = "./data/tweets_dataset.csv"
df = pd.read_csv(data_url)

df = DataCleaner(df).getData()
df = df[['Text', 'Biased']]


json_bulder = JsonBulder(df)
