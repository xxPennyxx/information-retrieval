import nltk
import numpy as np
import re

# nltk.download('words')
# nltk.download('punkt')

from nltk.util import ngrams

def tokenize_re(doc):
    words = re.findall(r'\b\w+\b', doc.casefold())
    return words
with open('IR/Jay.txt','r') as fp:
    jay=fp.read()
with open('IR/Gloria.txt','r') as fp:
    gloria=fp.read()
with open('IR/Claire.txt','r') as fp:
    claire=fp.read()
with open('IR/Phil.txt','r') as fp:
    phil=fp.read()
with open('IR/Haley.txt','r') as fp:
    haley=fp.read()
with open('IR/Alex.txt','r') as fp:
    alex=fp.read()
with open('IR/Mitchell.txt','r') as fp:
    mitchell=fp.read()
with open('IR/Cameron.txt','r') as fp:
    cameron=fp.read()
with open('IR/Manny.txt','r') as fp:
    manny=fp.read()
with open('IR/Luke.txt','r') as fp:
    luke=fp.read()
with open('IR/Lily.txt','r') as fp:
    lily=fp.read()

corpus=[]

for x in tokenize_re(jay):
    corpus.append(x)
for x in tokenize_re(gloria):
    corpus.append(x)
for x in tokenize_re(claire):
    corpus.append(x)
for x in tokenize_re(phil):
    corpus.append(x)
for x in tokenize_re(mitchell):
    corpus.append(x)
for x in tokenize_re(cameron):
    corpus.append(x)
for x in tokenize_re(haley):
    corpus.append(x)
for x in tokenize_re(alex):
    corpus.append(x)
for x in tokenize_re(manny):
    corpus.append(x)
for x in tokenize_re(luke):
    corpus.append(x)
for x in tokenize_re(lily):
    corpus.append(x)

def jaccard_coefficient(set1, set2):
    return len(set1.intersection(set2)) / len(set1.union(set2))

def generate_kgrams(word, k):
    word = word.casefold()
    kgrams = list(ngrams(word, k))
    # generating n-grams for each and every word in the corpus
    return [''.join(kgram) for kgram in kgrams]

def correct_spelling(word):
    if word in corpus:
        return word

    k = 2  
    word_kgrams = set(generate_kgrams(word, k))
    # print(word_kgrams)
    similarities = [(w, jaccard_coefficient(word_kgrams, set(generate_kgrams(w, k)))) for w in corpus]
    suggestions = sorted(similarities, key=lambda x: x[1], reverse=True)
    most_similar_word, _ = suggestions[0]

    return most_similar_word

input_word= input("Enter a misspelled word to check spelling: ")
corrected = correct_spelling(input_word)
print("Input word:",input_word)
print("Suggested word:",corrected)
