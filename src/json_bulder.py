import pandas as pd
import numpy as np
import json

from df_exploration import DfExploration

class JsonBulder:
    def __init__(self,df):
        self.df = df
        self.json_data = []
        self.build_json()

    def add_data(self, data):
        self.json_data.append(data)

    def build_json(self):
        df = self.df
        self.json_data = DfExploration.add_total_tweets(df)
        self.json_data = DfExploration.add_average_length(df)
        self.json_data = DfExploration.add_common_words(df)
        df['Text'] = df['Text'].str.join(' ')
        self.json_data = DfExploration.add_longest_3_tweets(df)
        self.json_data = DfExploration.add_num_upper_words(df)

        self.json_data = json.dumps(self.json_data)
        self.json_data = json.loads(self.json_data)
        self.save_json('results/result.json')


    def save_json(self, path):
        with open(path, 'w') as f:
            json.dump(self.json_data, f)



