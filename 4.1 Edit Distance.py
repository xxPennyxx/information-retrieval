import re
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


def edit_distance(word1,word2):
    m=len(word1)
    n=len(word2)
    table=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        table[i][0]=i
    for j in range(n+1):
        table[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1]==word2[j-1]:
                table[i][j]=table[i-1][j-1]
            else:
                table[i][j]=min(table[i-1][j],table[i][j-1],table[i-1][j-1])+1
    return table[m][n]

def correct_spelling(word):
    if word in corpus:
        return word
    similarities = [(w, edit_distance(word,w)) for w in corpus]
    suggestions = sorted(similarities, key=lambda x: x[1])
    most_similar_word, _ = suggestions[0]
    return most_similar_word

input_word= input("Enter a misspelled word to check spelling: ")
corrected = correct_spelling(input_word)
print("Input word:",input_word)
print("Suggested word:",corrected)

