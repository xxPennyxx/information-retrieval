import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re

nltk.download('punkt')


def tokenize(doc):
    sentences=sent_tokenize(doc)
    words=word_tokenize(doc)

    return sentences, words

def tokenize_re(doc):
    # Use regular expression to split text into words
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
s,w=tokenize(claire)
print(w)
print(tokenize_re(haley))

