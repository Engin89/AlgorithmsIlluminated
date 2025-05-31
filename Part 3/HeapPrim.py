import time
import functools
import heapq
from random import randint

with open("problem15.9test2.txt", 'r') as input:
    lines = input.readlines()

lengths = {}
vertices = []
temp_list = []
for line in lines[1:]:
    contents = line.split("\n")
    contents = [*filter(lambda x: x != '', contents)]
    temp_list.extend(contents)

contents = [*map(lambda x: x.split(" "), temp_list)]
lengths = {f'{content[0]}-{content[1]}': int(content[2]) for content in contents}
for content in contents:
    lengths[f'{content[1]}-{content[0]}'] = int(content[2])
vertices = [*set([int(content[0]) for content in contents]).union(set([int(content[1]) for content in contents]))]



def Prim(vertices, lengths):
    h = []
    costs = {}
    T = {}
    start = randint(0, len(vertices));
    s = vertices[start]
    X = [s]
    winner = {}
    for vertex in vertices:
        if lengths.get(f"{s}-{vertex}") is not None:
            costs[vertex] = lengths[f"{s}-{vertex}"]
            winner[vertex] = f"{s}-{vertex}"
        else:
            costs[vertex] = 999999999999999999999
            winner[vertex] = ""
        heapq.heappush(h, (costs[vertex], vertex))
    while len(h) > 0:
        w = heapq.heappop(h)
        X.append(w[1])
        T[w[1]] = [winner[w[1]], costs[w[1]]]
        Y = set(vertices).difference(X)
        for y in Y:
            key = f"{w[1]}-{y}"
            if lengths.get(key) is not None:
                if lengths[key] < costs[y]:
                    h.remove((costs[y], y))
                    costs[y] = lengths[key]
                    winner[y] = key
                    heapq.heappush(h, (costs[y], y))
    del T[s]
    total = functools.reduce(lambda a, b: a+b, [v[1] for k, v in T.items() if v[1] != 999999999999999999999])
    return total


start_time = time.time()
print(Prim(vertices=vertices, lengths=lengths))
print(time.time() - start_time, "seconds")

