from collections import defaultdict
from itertools import groupby
file=open('C:/Users/aless/PycharmProjects/4th-Assignment/words_alpha.txt')
dic=file.read().splitlines()
file.close()
d=defaultdict(list)
for word in dic:
    d[len(word)].append(word)

def hdistance(x,y):
    n=sum(1 for i,j in zip(x,y) if i!=j)
    return n

def EquivalentWords(start,finish):
    l=d[len(start)]
    hd=hdistance(start,finish)
    dict=defaultdict(list)
    for i in range(1,hd):
        j=hd-i
        for ind,word in enumerate(l):
            if hdistance(start,word)==i and hdistance(finish,word)==j:
                dict[i].append(word)
    return dict

alll=EquivalentWords('bounce','kettle')
print(alll)
#this code works only in a straight line and to accept some deviations it should be faced recursively in a process that would require to many comparisons
