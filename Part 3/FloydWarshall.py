import numpy as np
with open("problem18.8test1.txt", 'r') as input_value:
    lines = input_value.readlines()

lengths = {}
vertices = []
temp_list = []
for line in lines[1:]:
    contents = line.split("\n")
    contents = [*filter(lambda x: x != '', contents)]
    temp_list.extend(contents)

contents = [*map(lambda x: x.split(" "), temp_list)]
lengths = {f'{int(content[0])}-{int(content[1])}': int(content[2]) for content in contents}
vertices_num = int(line.split(" ")[0])


def FloydWarshall(adj_list, n):
    A = np.zeros((n+1, n+1, n+1), dtype = float)
    for v in range(1,n+1):
        for w in range(1, n+1):
            if v == w:
                A[0, v, w] = 0
            elif adj_list.get(f'{v}-{w}') is not None:
                A[0, v, w] = adj_list[f'{v}-{w}']
            else:
                A[0, v, w] = np.Inf
    for k in range(1, n+1):
        for v in range(1,n+1):
            for w in range(1, n+1):
                A[k,v,w] = min(A[k-1, v, w], A[k-1, v, k] + A[k-1, k, w])
    for v in range(n):
        if A[n, v, v] < 0:
            return "negative cycle"
    return A[n, :, :]


print(FloydWarshall(lengths, vertices_num))