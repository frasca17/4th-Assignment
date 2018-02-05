from collections import defaultdict
import networkx as nx
from itertools import combinations

file = open('words_alpha.txt')
dictionary = file.read().splitlines()
file.close()

#grouped all the words in the dictionary on the base of their lenght in a set of sudictionaries, need to do so for speeding up the simple version
subdicts = defaultdict(list)
for word in dictionary:
    subdicts[len(word)].append(word)

def equivalentWords(first, last):
    '''Converts first into last (words of same lenght) only by one substitution at a time substitution
    and only if the intermediate steps of the pathway are present in the dictionary of english words words_alpha.txt.
    Returns the pathway'''

    if len(first)!=len(last):
        raise ValueError('Words inserted are of different lengths, no possible path only substituting letters')

    #Protograph construction:

    subdict = subdicts[len(first)]
    protograph = {}
    for word in subdict:
        clusters = []
        for i in range(len(word)):
            clusters.append(word[:i] + '*' + word[i + 1:])
        for cluster in clusters:
            if cluster not in protograph:
                protograph[cluster] = [word]
            elif word not in protograph[cluster]:
                protograph[cluster].append(word)

    #Graph construction:

    G = nx.Graph()
    for cluster in protograph.keys():
        G.add_edges_from(combinations(protograph[cluster], 2))

    path=nx.shortest_path(G,first,last)

    return path


#Just an example:
print(' --> '.join(equivalentWords('kettle','bounce')))

