import re
from collections import defaultdict
import numpy as np
def tokenize_re(doc):
    words = re.findall(r'\b\w+\b', doc.casefold())
    return words

def create_inverted_index(docs):
    inverted_index = defaultdict(list)
    for id, doc in enumerate(docs):
        words = tokenize_re(doc)
        for w in words:
            inverted_index[w].append(id)
    return inverted_index

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

inverted_index = create_inverted_index([jay,gloria,claire,phil,mitchell,cameron,haley,alex,manny,lily,luke])
print("Complete inverted index:")
for term, doc_ids in sorted(inverted_index.items()):
    print(f"{term}: {np.unique(list(doc_ids))}")


