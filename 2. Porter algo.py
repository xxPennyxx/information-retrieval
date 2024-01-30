import re
def tokenize_re(doc):
    words = re.findall(r'\b\w+\b', doc.casefold())
    return words


def cv(word):
    seq=[]
    word=word.casefold()
    for l in word:
        if l in [*'aeiou']:
            seq.append('v')
        else:
            seq.append('c')
    return seq
def count_cv(word):
    seq=cv(word)
    m=0
    for i in range(len(seq)-1):
        if seq[i]=='v' and seq[i+1]=='c':
            m+=1
    return m

def normalize(word,input,output):
    temp=word.index(input)
    word=word[:temp]+output
    return word

def step_1a(word):
    if(word.endswith('sses')):
        word=normalize(word,'sses','ss')
    if(word.endswith('ies')):
        word=normalize(word,'ies','i')
    if(word.endswith('ss')):
        word=normalize(word,'ss','ss')
    if(word.endswith('s')):
        word=normalize(word,'s','s')
    return word



def step_1b(word):
    if(count_cv(word)>0 and word.endswith('eed')):
        word=normalize(word,'eed','ee')

    if word.endswith('ed'):
        temp=word[:word.index('ed')]
        if 'v' in cv(temp):
            word=normalize(word,'ed','')
            if(len(word)>=2 and word[-1]==word[-2] and word[-1] not in [*'lsz']):
                word=word[:-1]
            if(len(word)>=3 and count_cv(word)==1 and cv(word)[-3:]==['c','v','c'] and word[-1]!='w' and word[-1]!='x' and word[-1]!='y'):
                word=word+'e'
        else:
            pass
        
        
    if word.endswith('ing'):
        temp=word[:word.index('ing')]
        if 'v' in cv(temp):
            word=normalize(word,'ing','')
            if(len(word)>=2 and word[-1]==word[-2] and word[-1] not in [*'lsz']):
                word=word[:-1]
            if(len(word)>=3 and count_cv(word)==1 and cv(word)[-3:]==['c','v','c'] and word[-1]!='w' and word[-1]!='x' and word[-1]!='y'):
                word=word+'e'
        else:
            pass
    if word.endswith('at'):
        word=normalize(word,'at','ate')
    if word.endswith('bl'):
        word=normalize(word,'bl','ble')
    if word.endswith('iz'):
        word=normalize(word,'iz','ize')
    
    
        return word
    # m=1, cvc, last char should not be w,x,y
    
    return word

def step_1c(word):
    if word.endswith('y'):
        temp=word[:word.index('y')]
        if 'v' in cv(temp):
            word=normalize(word,'y','i')
        else:
            pass
    return word
def normalize1(word,input,output):
    if(word.endswith(input)):
        temp=word[:word.index(input)]
        if(count_cv(temp)>0):
            word=normalize(word,input,output)
            # word=temp+output
    return word

def step_2(word):
    if word.endswith('ational'):
        word=normalize1(word,'ational','ate')
    if word.endswith('tional'):
        word=normalize1(word,'tional','tion')
    if word.endswith('enci'):
        word=normalize1(word,'enci','ence')
    if word.endswith('anci'):
        word=normalize1(word,'anci','ance')
    if word.endswith('izer'):
        word=normalize1(word,'izer','ize')
    if word.endswith('iser'):
        word=normalize1(word,'iser','ise')
    if word.endswith('abli'):
        word=normalize1(word,'abli','able')
    if word.endswith('alli'):
        word=normalize1(word,'alli','al')
    if word.endswith('entli'):
        word=normalize1(word,'entli','ent')
    if word.endswith('eli'):
        word=normalize1(word,'eli','e')
    if word.endswith('ousli'):
        word=normalize1(word,'ousli','ous')
    if word.endswith('ization'):
        word=normalize1(word,'ization','ize')
    if word.endswith('ation'):
        word=normalize1(word,'ation','ate')
    if word.endswith('ator'):
        word=normalize1(word,'ator','ate')
    if word.endswith('alism'):
        word=normalize1(word,'alism','al')
    if word.endswith('iveness'):
        word=normalize1(word,'iveness','ive')
    if word.endswith('fulness'):
        word=normalize1(word,'fulness','ful')
    if word.endswith('ousness'):
        word=normalize1(word,'ousness','ous')
    if word.endswith('aliti'):
        word=normalize1(word,'aliti','al')
    if word.endswith('iviti'):
        word=normalize1(word,'iviti','ive')
    if word.endswith('biliti'):
        word=normalize1(word,'biliti','ble')
    return word

def step_3(word):
    if word.endswith('icate'):
        word=normalize1(word,'icate','ic')
    if word.endswith('ative'):
        word=normalize1(word,'ative','')
    if word.endswith('alize'):
        word=normalize1(word,'alize','al')
    if word.endswith('iciti'):
        word=normalize1(word,'iciti','ic')
    if word.endswith('ical'):
        word=normalize1(word,'ical','ic')
    if word.endswith('ness'):
        word=normalize1(word,'ness','')
    if word.endswith('ful'):
        word=normalize1(word,'ful','')
    
    return word

def normalize2(word,input,output):
    if(word.endswith(input)):
        temp=word[:word.index(input)]
        if(count_cv(temp)>1):
            word=normalize(word,input,output)
            # word=temp+output
    return word

def step_4(word):
    if word.endswith('al'):
        word=normalize2(word,'al','')
    if word.endswith('ance'):
        word=normalize2(word,'ance','')
    if word.endswith('ence'):
        word=normalize2(word,'ence','')
    if word.endswith('er'):
        word=normalize2(word,'er','')
    if word.endswith('ic'):
        word=normalize2(word,'ic','')
    if word.endswith('able'):
        word=normalize2(word,'able','')
    if word.endswith('ible'):
        word=normalize2(word,'ible','')
    if word.endswith('ant'):
        word=normalize2(word,'ant','')
    if word.endswith('ement'):
        word=normalize2(word,'ement','')
    if word.endswith('ment'):
        word=normalize2(word,'ment','')
    if word.endswith('ent'):
        word=normalize2(word,'ent','')
    if word.endswith('sion') or word.endswith('tion'):
        word=normalize2(word,'ion','')
    if word.endswith('ou'):
        word=normalize2(word,'ou','')
    if word.endswith('ism'):
        word=normalize2(word,'ism','')
    if word.endswith('ate'):
        word=normalize2(word,'ate','')
    if word.endswith('iti'):
        word=normalize2(word,'iti','')
    if word.endswith('ous'):
        word=normalize2(word,'ous','')
    if word.endswith('ive'):
        word=normalize2(word,'ive','')
    if word.endswith('ize'):
        word=normalize2(word,'ize','')
    return word

def step_5a(word):
    if word.endswith('e'):
        temp=word[:word.index('e')]
        if count_cv(temp)>1:
            word=normalize2(word,'e','')
        elif(len(temp)>=3 and count_cv(temp)==1 and cv(temp)[-3:]==['c','v','c'] and temp[-1]!='w' and temp[-1]!='x' and temp[-1]!='y'):
            word=normalize2(word,'e','')
    return word

def step_5b(word):
    if (count_cv(word)>1 and word[-1]==word[-2] and word[-1]=='l'):
        word=word[:-1]
    return word

def porters_algorithm(doc):
    res=[]
    for w in doc:
        # print("Tokenizing "+w)
        temp=step_1a(w)
        temp=step_1b(temp)
        temp=step_1c(temp)
        temp=step_2(temp)
        temp=step_3(temp)
        temp=step_4(temp)
        temp=step_5a(temp)
        temp=step_5b(temp)
        res.append(temp)
    return res
with open('IR/Jay.txt','r') as fp:
    jay=fp.read()
jay_tokens=tokenize_re(jay)
normalized=porters_algorithm(jay_tokens)
print(jay_tokens)
print(normalized)




















