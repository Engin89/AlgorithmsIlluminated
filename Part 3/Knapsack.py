import numpy as np

with open("problem16.7test.txt", 'r') as infile:
    freqs = infile.read()
graph = freqs.split("\n")
values = [[*map(int, i.split(' '))][0] for i in graph[:-1]]
sizes = [[*map(int, i.split(' '))][1] for i in graph[:-1]]

sizes_num = values.pop(0)
values_num = sizes.pop(0)


def knapsack(value_set, size_set, n, capacity):
    A = np.zeros((n, capacity), dtype=int)
    for i in range(1, n):
        for c in range(capacity):
            if size_set[i] > c:
                # print(i, c, capacity, n, size_set[i])
                A[i][c] = A[i - 1][c]
            else:
                A[i][c] = max(A[i - 1][c], A[i - 1][c - size_set[i]] + value_set[i])
    return A


def knapsack_reconstruction(A, value_set, size_set, capacity, n):
    S = []
    c = capacity - 1
    i = n - 1
    while i > 0:
        if size_set[i] <= c and A[i - 1][c - size_set[i]] + value_set[i] >= A[i - 1][c]:
            S.append(c)
            c -= size_set[i]
        i -= 1
    return S


knapsack_values = knapsack(values, sizes, values_num, sizes_num)
print(knapsack_reconstruction(knapsack_values, values, sizes, sizes_num, values_num))
