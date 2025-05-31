with open("problem16.6_v2.txt", 'r') as infile:
    freqs = infile.read()
graph = [*map(int, freqs.split("\n")[:-1])]
length = graph.pop(0)


def WIS(vertices, n):
    A = [vertices[0], vertices[1]]
    for i in range(2, n):
        temp = max(A[i-1], A[i-2] + vertices[i])
        A.append(temp)
    return A


wis_array = (WIS(graph, length))


def wis_reconstruction(vertices, a, n):
    S = []
    i = n-1
    while i >= 2:
        if a[i-1] >= a[i-2] + vertices[i]:
            i -= 1
        else:
            S.append(i)
            i -= 2
    if i == 1:
        S.append(i)
    return S


print(wis_reconstruction(graph, wis_array, length))