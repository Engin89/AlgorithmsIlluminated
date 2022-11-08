import numpy as np

testarr = [1, 15, 6, 4, 2, 0, 8, 10]


def ChoosePivot(n):
    p = np.random.randint(n)
    return p


def swap(A, pivot, left):
    x = A[pivot]
    A[pivot] = A[left]
    A[left] = x
    return A


def partition(arr, l, r):
    p = arr[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < p:
            arr = swap(arr, i, j)
            i += 1
    arr = swap(arr, l, i - 1)
    return i - 1, arr


def rselect(arr, pos):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        i = ChoosePivot(n)
        l, r = 0, n-1
        arr = swap(arr, i, l)
        j, arr = partition(arr, l, r)
        if j == pos:
            return arr[pos]
        elif j > pos:
            return rselect(arr[:j], pos)
        else:
            return rselect(arr[j + 1:], pos - j - 1)


print(rselect(testarr, 3))
