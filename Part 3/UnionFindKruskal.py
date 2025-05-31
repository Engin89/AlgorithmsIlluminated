import functools
import time
from unionfind import unionfind

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
lengths = [(int(content[0]), int(content[1]), int(content[2])) for content in contents]
edges = [(int(content[0]), int(content[1])) for content in contents]

lengths = sorted(lengths, key=lambda x: x[2])
vertices = [*set([int(content[0]) for content in contents]).union(set([int(content[1]) for content in contents]))]


def convert_to_adj_dict(testarr):
    adj_dict = {}
    for edge in testarr:
        src, dest = edge
        if src not in adj_dict:
            adj_dict[src] = [dest]
        else:
            adj_dict[src].append(dest)
        if dest not in adj_dict:
            adj_dict[dest] = [src]
        else:
            adj_dict[dest].append(src)
    return adj_dict


graph = convert_to_adj_dict(edges)


def FastKruskal(graph, lengths):
    i = 1
    T = {}
    for k, v in graph.items():
        i += 1
    u = unionfind(i)
    for length in lengths:
        v = length[0]
        w = length[1]
        if not u.issame(v, w):
            T[f'{v}-{w}'] = length[2]
            u.unite(v,w)
    total = functools.reduce(lambda a, b: a + b,
                             [val for k, val in T.items()])
    return total


start_time = time.time()
print(FastKruskal(graph, lengths))
print(time.time() - start_time, "seconds")
