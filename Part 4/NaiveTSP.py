import time
import random
from collections import deque
with open("tsptest2.txt", 'r') as input:
    lines = input.readlines()

lengths = {}
vertices = []
temp_list = []
for line in lines[1:]:
    contents = line.split("\n")
    contents = [*filter(lambda x: x != '', contents)]
    temp_list.extend(contents)

contents = [*map(lambda x: x.split(" "), temp_list)]
straight_lengths = {f'{content[0]}-{content[1]}': int(content[2]) for content in contents}
reverse_lengths = {f'{content[1]}-{content[0]}': int(content[2]) for content in contents}
lengths = {**straight_lengths, **reverse_lengths}
graph = [(int(content[0]), int(content[1])) for content in contents]
#lengths = sorted(lengths, key=lambda x: x[2])

print(lengths)


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


vertices = list(convert_to_adj_dict(graph).keys())
isexplored = {}
total = 0

def DFS(dag, s, n):
    isexplored[s] = 1
    adj = dag[s]
    global total
    for v in adj:
        if isexplored.get(v) is None:
            total += lengths[f'{s}-{v}']
            DFS(dag, v, n)
        else:
            n *= 0
    if n == 0:
        return list(isexplored)[-1]
    else:
        return True


def TSP(graph, lengths,vertices):
    global total
    global isexplored
    lowest = 100000000
    for vertex in vertices:
        start = vertex
        temp_graph = convert_to_adj_dict(graph)
        queue = deque(temp_graph[vertex])
        for i in range(len(queue)):
            isexplored = {}
            total = 0
            queue.rotate(-1)
            temp_graph[vertex] = list(queue)
            last = DFS(temp_graph, vertex, 1)
            local_total = total + lengths[f'{start}-{last}']
            #print(f"Route is completed!, here is the distance: {local_total}, {start}-{last}")
            if local_total < lowest:
                lowest = local_total

    return lowest


print(TSP(graph, lengths, vertices))