import numpy as np

with open("problem17.8nw.txt", 'r') as infile:
    lines = infile.read()
    lines = lines.split("\n")

inputs = []
for line in lines:
    inputs.extend(line.split(" "))
inputs = [*filter(lambda x: x != '', inputs)]
length_x, length_y, gap_cost, mismatch_cost, X, Y = int(inputs[0]), int(inputs[1]),\
                                                    int(inputs[2]), int(inputs[3]),\
                                                    inputs[4], inputs[5]


def NW(x, y, alpha_gap, alpha_xy, m, n):
    A = np.zeros((m, n), dtype=float)
    for i in range(m):
        A[i][0] = i * alpha_gap
    for j in range(n):
        A[0][j] = j * alpha_gap
    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:
                mismatch = 0
            else:
                mismatch = 1
            A[i, j] = min(A[i-1, j-1] + mismatch * alpha_xy,
                          A[i-1, j] + alpha_gap,
                          A[i, j-1] + alpha_gap)
    return A


def NW_reconstruction(A, m, n, x, y):
    x_set = []
    y_set = []
    i = m-1
    j = n-1
    while i >= 0:
        if A[i-1, j-1] < A[i-1, j] and A[i-1, j-1] < A[i, j-1]:
            x_set.append(x[i])
            y_set.append(y[j])
            i -= 1
            j -= 1
        elif A[i-1, j] < A[i-1, j-1] and A[i-1, j] < A[i, j-1]:
            x_set.append(x[i-1])
            y_set.append("--")
            i -= 1
        else:
            x_set.append("--")
            y_set.append(y[j-1])
            j -= 1

    return list(reversed(x_set)), list(reversed(y_set))


NW_array = NW(X, Y, gap_cost, mismatch_cost, length_x, length_y)
print(NW_reconstruction(NW_array, length_x, length_y, X, Y))


