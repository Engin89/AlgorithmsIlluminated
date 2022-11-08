import numpy as np

testarr = [6,4,3,2,1,0]


def ChoosePivot(arr, l, r):
    p = np.random.randint(l,r)
    return p


def swap(A, pivot, left):
    x = A[pivot]
    A[pivot] = A[left]
    A[left] = x
    return A


def partition(arr, l, r):
    p = arr[l]
    print(p, arr)
    i = l + 1
    for j in range(l + 1, r + 1):
        if arr[j] < p:
            arr = swap(arr, i, j)
            i += 1
    print(arr)
    arr = swap(arr, l, i - 1)
    print(arr, i - 1)
    return i - 1


def quicksort(arr, l, r):
    if l >= r:
        return arr
    else:
        i = ChoosePivot(arr, l, r)
        arr = swap(arr, i, l)
        j = partition(arr, l, r)
        quicksort(arr, l, max(j - 1, 0))
        quicksort(arr, j + 1, max(0, r))
        return arr


print(quicksort(testarr, 0, len(testarr)-1))
