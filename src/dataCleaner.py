import pandas as pd

class DataCleaner:

# get data in format of dataframe and clean
    def cleanData(self, data):
        df = pd.DataFrame(data)

    def cleanNaN(self, df):
        df = df.dropna()
        return df

    def cleanDuplicate(self, df):
        df = df.drop_duplicates()
        return df

    def CleaningCommas(self, df):
        df = df.replace(',', '', regex=True)

