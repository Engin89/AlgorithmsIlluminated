from collections import deque
import random

with open("tsptest2.txt", 'r') as input:
    lines = input.readlines()

lengths = {}
vertices = [1]
temp_list = []
for line in lines[1:]:
    contents = line.split("\n")
    contents = [*filter(lambda x: x != '', contents)]
    temp_list.extend(contents)

contents = [*map(lambda x: x.split(" "), temp_list)]
straight_lengths = {f'{content[0]}-{content[1]}': int(content[2]) for content in contents}
reverse_lengths = {f'{content[1]}-{content[0]}': int(content[2]) for content in contents}
lengths = {**straight_lengths, **reverse_lengths}
contents = sorted([[*map(int, content)] for content in contents], key=lambda x: x[2])
graph = [(int(content[0]), int(content[1])) for content in contents]
vertices = [*set([int(content[1]) for content in contents])]
# lengths = sorted(lengths, key=lambda x: x[2])

isexplored = {}
total = 0
route = []

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


def DFS(dag, s, n):
    isexplored[s] = 1
    adj = dag[s]
    global total
    global route
    for v in adj:
        if isexplored.get(v) is None:
            total += lengths[f'{s}-{v}']
            print(s, v, total)
            route.append(f'{s}-{v}')
            DFS(dag, v, n)
            break
        else:
            n *= 0
    if n == 0:
        return list(isexplored)[-1]
    else:
        return list(isexplored)[-1]


def NearestNeighborTSP(graph, lengths, start_ix):
    vertices = list(convert_to_adj_dict(graph).keys())
    adj_list = convert_to_adj_dict(graph)
    start = start_ix
    global total
    global isexplored
    isexplored = {}
    temp_adj = adj_list[start]
    queue = deque(temp_adj)
    queue.rotate(-1)
    temp_adj = list(queue)
    last = DFS(adj_list, start, 1)

    total += lengths[f'{start}-{last}']
    route.append(f'{last}-{start}')
    return route, total


# print(NearestNeighborTSP(graph, lengths, 3))
def swap_edges(tour, old, new):
    temp = '?'
    new_tour = [edge.replace(new, temp) for edge in tour]
    new_tour = [edge.replace(old, new) for edge in new_tour]
    new_tour = [edge.replace(temp, old) for edge in new_tour]
    return new_tour


def two_OPT(tour, cost, lengths, vertices):
    next_tour = tour
    my_vertices = len(vertices)
    temp_list = [*range(my_vertices)]
    a = random.choice(temp_list)
    temp_list.remove(a)
    b = random.choice(temp_list)
#vw -> vx
#ux -> uw
    first = next_tour[a]
    last = next_tour[b]
    v = first.split('-')[0]
    w = first.split('-')[1]
    u = last.split('-')[0]
    x = last.split('-')[1]
    #print(v,w,u,x)
    if lengths.get(f'{u}-{w}') is not None and lengths.get(f'{v}-{x}') is not None:
        decrease = lengths[f'{v}-{w}'] + lengths[f'{u}-{x}'] - lengths[f'{x}-{w}'] - lengths[f'{v}-{u}']
        next_tour = swap_edges(next_tour, w, u)
        cost -= decrease
    else:
        decrease = None
    return next_tour, cost, decrease


initial_tour, cost = NearestNeighborTSP(graph, lengths, 1)
min_cost = 1000
i = 50
while i > 0:
    #print(initial_tour, cost, i)
    new_tour, new_cost, new_decrease = two_OPT(initial_tour, cost, lengths, vertices)
    initial_tour = new_tour
    cost = new_cost
    if cost < min_cost:
        min_cost = new_cost
        min_tour = new_tour
    i -= 1

print(min_tour, min_cost)