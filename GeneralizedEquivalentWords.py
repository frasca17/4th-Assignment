import networkx as nx
from itertools import combinations

file = open('words_alpha.txt')
dictionary = file.read().splitlines()
file.close()

def equivalentWords(first, last):
    '''Converts first into last. The conversion can occur only by one substitution, or an insertion, or a deletion at a time
    and only if the intermediate steps of the pathway are present in the dictionary of english words words_alpha.txt.
    Returns the pathway'''

    #Protograph construction:

    protograph = {}
    for word in dictionary:
        clusters = ['*'+word]
        for i in range(len(word)):
            clusters.append(word[:i] + '*' + word[i + 1:])
            clusters.append(word[:i + 1] + '*' + word[i + 1:])
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
print(' --> '.join(equivalentWords('spider','man')))