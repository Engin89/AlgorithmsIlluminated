import functools
import time

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
lengths = sorted(lengths, key=lambda x: x[2])

isexplored = {}


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
    for v in adj:
        if isexplored.get(v) is None:
            DFS(dag, v, n)
        else:
            n *= 0
    if n == 0:
        return False
    else:
        return True


def Kruskal(lengths):
    T = {}
    temp = []
    start = lengths[0][0]
    for length in lengths:
        global isexplored
        isexplored = {}
        x = length[0]
        y = length[1]
        temp.append((x, y))
        temp_dict = convert_to_adj_dict(temp)
        NonCyclical = DFS(temp_dict, start, 1)
        if NonCyclical:
            T[f'{x}-{y}'] = length[2]
        else:
            temp.pop()
    total = functools.reduce(lambda a, b: a + b,
                             [val for k, val in T.items()])
    return total, T


start_time = time.time()
print(Kruskal(lengths))
print(time.time() - start_time, "seconds")
