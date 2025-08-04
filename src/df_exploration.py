import pandas as pd
import numpy as np
class DfExploration:

    # "total_tweets": {
    #     "antisemitic": 512,
    #     "non_antisemitic": 741,
    #     "total": 12800,
    #     <unspecified>: 27
    # },
    @staticmethod
    def add_total_tweets(df):
        key = {0: 'antisemitic', 1: 'non_antisemitic'}
        dict = {}
        dict['total_tweets'] = {}
        # how meny tweets in the dataset
        dict['total_tweets']['total'] = float(df.shape[0])
        # how many tweets in each bias category
        for bias in df['Biased'].unique():
            dict['total_tweets'][key[bias]] = float(df.groupby('Biased').size()[bias])
        dict['total_tweets']['unspecified'] = float(dict['total_tweets']['total'] - dict['total_tweets']['antisemitic'] - \
                                              dict['total_tweets']['non_antisemitic'])
        return dict

    # "average_length": {
    #         "antisemitic": 18.3,
    #         "non_antisemitic": 20.7,
    #         "total": 24.2
    #     },
    @staticmethod
    def add_average_length(df):
        key = {0: 'antisemitic', 1: 'non_antisemitic'}
        dict = {}
        dict['average_length'] = {}
        for bias in df['Biased'].unique():
            dict['average_length'][key[bias]] = float(df[df['Biased'] == bias]['lengths'].mean())
        dict['average_length']['total'] = float(df['lengths'].mean())
        return dict


    # "common_words": {
    #     "total": ["the","and","is","to","jews","support","zionists","peace","fight","truth"]
    # },

    @staticmethod
    def add_common_words(df,num_words=10):
        dict = {}

        words = {}
        for text in df['Text']:
            for word in text:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
        result = []
        sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
        for word in sorted_words[:10]:
            result.append(word[0])
        dict['common_words'] = result
        return dict

    # "longest_3_tweets": {
    #     "antisemitic": [
    #         "Zionists control everything and lie about the holocaust for sympathy and power. Wake up, world.",
    #         "Jews are manipulating global politics again. Open your eyes, they’ve done this before.",
    #         "The media is owned by Zionists, they spread lies daily. Don’t believe anything they say!"
    #     ],
    #     "non_antisemitic": [
    #         "Today we honor all communities and stand against hate. Peace and unity are stronger than division.",
    #         "I’m proud to support equal rights for all people, regardless of religion, race or belief.",
    #         "Education is the best way to fight ignorance and bigotry. We must keep learning and listening."
    #     ]
    # },
    @staticmethod
    def add_longest_3_tweets(df):
        key = {0: 'antisemitic', 1: 'non_antisemitic'}
        dict = {}
        dict['longest_3_tweets'] = {}
        for bias in df['Biased'].unique():
            dict['longest_3_tweets'][key[bias]] = df[df['Biased'] == bias].head(3)['Text'].tolist()
        return dict

    # "uppercase_words": {
    #     "antisemitic": 139,
    #     "non_antisemitic": 86,
    #     "total": 421
    # }

    @staticmethod
    def add_num_upper_words(df):
        key = {0: 'antisemitic', 1: 'non_antisemitic'}
        dict = {}
        dict['uppercase_words'] = {}

        for bias in df['Biased'].unique():
            for text in df[df['Biased'] == bias]['Text']:
                for word in text:
                    if word.isupper():
                        if key[bias] not in dict['uppercase_words']:
                            dict['uppercase_words'][key[bias]] = 1
                        else:
                            dict['uppercase_words'][key[bias]] += 1
        dict['uppercase_words']['total'] = dict['uppercase_words']['antisemitic'] + dict['uppercase_words']['non_antisemitic']
        return dict