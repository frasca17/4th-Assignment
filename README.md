# 4th-Assignment

Simplified Equivalent Words: 
Our task is to transform one English word s into another word t by going
through a series of steps of English words, contained in a dictionary(we already provided here the dictionary 'words_alpha.txt'), where each word in the sequence differs from the next by only one substitution, so just one character varies(for instance, to transform head into tail the path is: head → heal → teal → tell → tall → tail).

Generalized Equivalent Words:
Our task in very similar to that asked in the previous problem but now we are in the more general case in which not only susbstitution is allowed to go from a word s to a word t, but also insertions and deletions(for instance, to transform head into tea is shown the following path: head → heal → teal → tea)

To solve these tasks we used the Graph Theory, in particular Undirected Graphs.

Two players play the following game with a nucleotide sequence of
length n = nA + nT + nC + nG , where nA, nT , nC , and nG are the
number of A,T,C, and G in the sequence. At every turn a player
may delete either one or two nucleotides from the sequence. The
player who is left with a uni-nucleotide sequence of an arbitrary
length (i.e., the sequence containing only one of 4 possible
nucleotides) loses. Who will win? Describe the winning strategy
for each nA, nT , nC , and nG .

For further informations please visit our Wiki
