#First, we will have to download spacy library
import spacy


#We will have to load large english language corpora in spacy
nlp = spacy.load('en_core_web_lg')

#printing out the vector of 300 dimensions of the following unicode string
print(nlp(u"The quick brown fox jumped").vector)

#exploring similarities between tokens

tokens = nlp(u"lion cat pet")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


#The following function will tell us the size of the vocabulary in spacy

print(nlp.vocab.vectors.shape)

tokens2 = nlp(u"dog cat Uzbekistan")

for token in tokens2:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


from scipy import spatial

cosine_similarity = lambda vec1, vec2: 1- spatial.distance.cosine(vec1, vec2)
king = nlp.vocab['king'].vector
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector
new_vector = king - man + woman

computed_similarities = []

for word in nlp.vocab:
    if word.has_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity = cosine_similarity(new_vector, word.vector)
                computed_similarities.append((word, similarity))

computed_similarities = sorted(computed_similarities, key = lambda item: -item[1])
print('\n')
print([x[0]for x in computed_similarities[:10]])
