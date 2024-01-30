import re
import numpy as np
def tokenize_re(doc):
    words = re.findall(r'\b\w+\b', doc.casefold())
    return words

class PostingList:
    def __init__(self,docids):
        self.docids=docids
    def intersect(self,set2):
        res=[]
        i=0
        j=0
        while i<len(self.docids) and j<len(set2.docids):
            if self.docids[i]==set2.docids[j]:
                res.append(self.docids[i])
                i+=1
                j+=1
            elif self.docids[i]<set2.docids[j]:
                i+=1
            else:
                j+=1
        return PostingList(res)
    def union(self,set2):
        res=[]
        i=0
        j=0
        while i<len(self.docids) and j<len(set2.docids):
            if self.docids[i]==set2.docids[j]:
                res.append(self.docids[i])
                i+=1
                j+=1
            elif self.docids[i]<set2.docids[j]:
                res.append(self.docids[i])
                i+=1
            else:
                res.append(set2.docids[j])
                j+=1
        res.extend(self.docids[i:])
        res.extend(set2.docids[j:])
        return PostingList(res)
    
class InvertedIndex:
    def __init__(self):
        self.index={}
    def add_document(self,docid,terms):
        for term in terms:
            if term not in self.index:
                self.index[term]=PostingList([]) #Create new posting list if term not already there
            self.index[term].docids.append(docid) #Append the document ID to the corresponding term index
    def process_query(self,query):
        query=query.split()
        result=None
        terms=[query[0],query[2]]
        if query[1]=='OR':
            for term in terms:
                if term in self.index:
                    if result is None:
                        result=self.index[term]
                    else:
                        result=result.union(self.index[term])
                else:
                    if result is None:
                        result=PostingList([])
        elif query[1]=='AND':
            for term in terms:
                if term in self.index:
                    if result is None:
                        result=self.index[term]
                    else:
                        result=result.intersect(self.index[term])
                else:
                    if result is None:
                        result=PostingList([])

        if result:
            return result.docids
        else:
            return []

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


i=InvertedIndex()
i.add_document(1,tokenize_re(jay))
i.add_document(2,tokenize_re(gloria))
i.add_document(3,tokenize_re(claire))
i.add_document(4,tokenize_re(phil))
i.add_document(5,tokenize_re(mitchell))
i.add_document(6,tokenize_re(cameron))
i.add_document(7,tokenize_re(haley))
i.add_document(8,tokenize_re(alex))
i.add_document(9,tokenize_re(manny))
i.add_document(10,tokenize_re(luke))
i.add_document(11,tokenize_re(lily))

term1=input("Enter a term: ").casefold()
term2=input("Enter another term: ").casefold()
boolquery=input("Enter a Boolean query (AND/OR): ").upper()
res=i.process_query(term1+" "+boolquery+" "+term2)
print("Documents that match the query:", np.unique(res))

        