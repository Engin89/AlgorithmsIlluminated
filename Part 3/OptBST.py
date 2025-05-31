import numpy as np

with open("problem17.8optbst.txt", 'r') as infile:
    lines = infile.read()
    lines = lines.split("\n")

key_size = int(lines[0])
frequencies = [*map(int, lines[1].split(","))]
keys = [*range(50)]
pairs = [*zip(keys,frequencies)]

prob17_4 = [(1,20),(2,5), (3,17), (4,10), (5,20), (6,3), (7,25)]


def optBST(n, pairs):
    A = np.zeros((n+1, n+1), dtype=int)
    for i in range(0, n):
        A[i, i] = 0
    for s in range(0, n):
        for i in range(0, n-s):
            minimum = float('Inf')
            total_freq = 0
            for r in range(i, i + s + 1):
                candidate = A[i, r-1] + A[r + 1, i + s]
                if candidate < minimum:
                    minimum = candidate
            for k in range(i, i + s + 1):
                total_freq += pairs[k][1]
            A[i, i + s] = total_freq + minimum
    return A[0,n-1]


print(optBST(7, prob17_4))
