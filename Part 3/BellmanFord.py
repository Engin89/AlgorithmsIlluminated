import numpy as np
with open("problem18.8test1.txt", 'r') as input_value:
    lines = input_value.readlines()

vertices = []
temp_list = []
for line in lines[1:]:
    contents = line.split("\n")
    contents = [*filter(lambda x: x != '', contents)]
    temp_list.extend(contents)

contents = [*map(lambda x: x.split(" "), temp_list)]
lengths = [(int(content[0])-1, int(content[1])-1, int(content[2])) for content in contents]
vertices_num = int(lines[0].split(" ")[0])
vertices = [i for i in range(vertices_num)]
edges_num = int(lines[0].split(" ")[1].replace("\n", ""))


def convert_to_adj_dict(testarr):
    in_dict = {}
    for edge in testarr:
        src, dest, length = edge[0], edge[1], edge[2]
        if dest not in in_dict:
            in_dict[dest] = [(src, length)]
        else:
            in_dict[dest].append((src, length))
    return in_dict


def BellmanFord(graph, source, n, inflows, edges):
    A = np.zeros((n+1,n), dtype = float)
    A[0, source] = 0
    for k in vertices:
        if k != source:
            A[0, k] = np.Inf
    for i in range(1, n):
        for k in graph:
            if k != source:
                inner_min = np.Inf
                if inflows.get(k) is None:
                    A[i,k] = inner_min
                else:
                    for w in inflows[k]:
                        if w is not None:
                            start_node = w[0]
                            length = w[1]
                            if A[i-1, start_node]+length < inner_min:
                                inner_min = A[i-1, start_node]+length
                    if A[i-1,k] < inner_min:
                        A[i,k] = A[i-1,k]
                    else:
                        A[i,k] = inner_min
    for edge in edges:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        if A[n-1,v] > A[n-1, u] + w:
            return "negative cycle"
    return A[n-1,:]


incoming_dict = (convert_to_adj_dict(lengths))
print(BellmanFord(vertices, 1, vertices_num, incoming_dict, lengths))













