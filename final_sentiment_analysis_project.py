import nltk

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

a = 'This is a good movie'
print(sid.polarity_scores(a))

b = "This was the best, most awesome movie EVER MADE!!!"

print(sid.polarity_scores(b))

c = "This was the WORST movie that has ever disgraced the screen"

print(sid.polarity_scores(c))


import pandas as pd

df = pd.read_csv('amazonreviews.tsv', sep = '\t')

print(df.head())


print(df['label'].value_counts())


df.dropna(inplace= True)
blanks = []
for i,lb, rv in df.itertuples():
    #(index, label, review)
    if type(rv) == str:
        if rv.isspace():
            blanks.append(i)

print(blanks)

print(sid.polarity_scores(df.iloc[0]['review']))

df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))

print(df.head)

df['compound'] = df['scores'].apply(lambda d : d['compound'])

df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score  >=0 else 'neg')

print(df.head())

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print(accuracy_score(df['label'], df['comp_score']))

print(classification_report(df['label'], df['comp_score']))
