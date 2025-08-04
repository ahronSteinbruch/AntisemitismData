import pandas as pd

class DataCleaner:
    def __init__(self,df):
        self.df = df
        self.cleanNaN()
        self.cleanDuplicate()
        self.CleaningCommas()
        self.CleaningShtrudel()
    def getData(self):
        return self.df

    def cleanNaN(self):
        self.df = self.df.dropna()
        return self.df

    def cleanDuplicate(self):
        self.df = self.df.drop_duplicates()
        return self.df

    def CleaningCommas(self):
        self.df = self.df.replace(',', '', regex=True)

    def CleaningShtrudel(self):
        self.df = self.df.replace('@' '', regex=True)

    def cleanDuplicate(self):
        self.df = self.df.drop_duplicates(subset=['Text', 'Biased'], keep='first')


