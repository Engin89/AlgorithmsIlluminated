from collections import deque
import random
import numpy as np
from itertools import combinations
with open("tsptest2.txt", 'r') as input:
    lines = input.readlines()

lengths = {}
temp_list = []
for line in lines[1:]:
    contents = line.split("\n")
    contents = [*filter(lambda x: x != '', contents)]
    temp_list.extend(contents)

contents = [*map(lambda x: x.split(" "), temp_list)]
straight_lengths = {f'{int(content[0])-1}-{int(content[1])-1}': int(content[2]) for content in contents}
reverse_lengths = {f'{int(content[1])-1}-{int(content[0])-1}': int(content[2]) for content in contents}
lengths = {**straight_lengths, **reverse_lengths}
contents = sorted([[*map(int, content)] for content in contents], key=lambda x: x[2])
graph = [(int(content[0]), int(content[1])) for content in contents]
vertices = [*set([int(content[1])-1 for content in contents])]


def create_indices(vertices):
    i = 0
    indices = {}
    reverse_indices = {}
    subsets = {}
    for n in vertices:
        temp = []
        combs = combinations(vertices, n)
        for comb in combs:
            indices[i] = list(comb)
            reverse_indices[str(list(comb))] = i
            i += 1
            temp.append(i-1)
        subsets[n] = temp
    return indices, subsets, reverse_indices


def BellmanHeldKarp(n, lengths, vertices, ix, subsets, reverse_indices):

    A = np.zeros((2**(n-1)-1, n-1), dtype = float)
    for j in vertices:
        A[j-1,j-1] = lengths[f'0-{j}']
    for s in range(2, n):
        subset = subsets[s]
        for index in subset:
            minigraph = ix[index]
            for j in minigraph:
                backup = minigraph.copy()
                backup.remove(j)
                lookup = reverse_indices[str(backup)]
                min_val = 999999
                for k in minigraph:
                    if k != 0 and k != j:
                        temp_var = A[lookup, k-1] + lengths[f'{k}-{j}']
                        if temp_var < min_val:
                            min_val = temp_var
                A[index, j-1] = min_val
    shortest_round = 99999
    for j in vertices:
        final_temp = A[-1, j-1] + lengths[f'{j}-{0}']
        if final_temp < shortest_round:
            shortest_round = final_temp
    return shortest_round


indices, subsets, reverse_indices = create_indices(vertices)
print(BellmanHeldKarp(len(vertices)+1, lengths, vertices, indices, subsets, reverse_indices))
