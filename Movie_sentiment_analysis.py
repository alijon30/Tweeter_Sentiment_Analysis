import pandas as pd
import numpy as np


df = pd.read_csv('moviereviews.tsv', sep = '\t')

blanks = []

df.dropna(inplace=True)
print(df.head())
print(df['label'].value_counts())
for i, lb, rv in df.itertuples():
    if type(rv) == str:
        if rv.isspace():
            blanks.append(i)


df.drop(blanks, inplace=True)
print(df['label'].value_counts())

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

df['scores'] = df['review'].apply(lambda score: sid.polarity_scores(score))
df['compound'] = df['scores'].apply(lambda d: d['compound'])
df['comp_score'] = df['compound'].apply(lambda score : 'pos' if score >= 0 else 'neg')
print(df.head())

from sklearn.metrics import accuracy_score, classification_report

print(accuracy_score(df['label'], df['comp_score']))
