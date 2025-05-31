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
contents = sorted([[*map(int, content)] for content in contents], key = lambda x: x[2])
graph = [(int(content[0]), int(content[1])) for content in contents]
# lengths = sorted(lengths, key=lambda x: x[2])

isexplored = {}
total = 0

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
    for v in adj:
        if isexplored.get(v) is None:
            total += lengths[f'{s}-{v}']
            print(s, v, total)
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
    print(f'{start}-{last}')
    return total


print(NearestNeighborTSP(graph, lengths, 5))


