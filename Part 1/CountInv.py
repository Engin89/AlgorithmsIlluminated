import numpy as np
testarr = np.loadtxt("inversions.txt").tolist()


#testarr = [54044, 14108, 79294, 29649, 25260, 60660, 2995, 53777, 49689, 9083]


#testarr =  [1,3,5,2,4,6]

def CountSplitInv(left, right):
    n = len(left) + len(right)
    splitInv = 0
    sortedArr = []
    i = 0
    for k in range(0, n):
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sortedArr.append(left.pop(0))
                i += 1
            else:
                sortedArr.append(right.pop(0))
                splitInv += (int(n / 2) - i)
        elif len(left) == 0 and len(right) > 0 and len(sortedArr) < n:
            sortedArr.extend(right)

        elif len(right) == 0 and len(left) > 0 and len(sortedArr) < n:
            sortedArr.extend(left)
    return sortedArr, splitInv


def CountInv(arr):
    end = len(arr)
    if end <= 1:
        return arr, 0
    else:

        mid = int(end / 2)
        leftarr = arr[:mid]
        rightarr = arr[mid:]
        leftarr, leftInv = CountInv(leftarr)
        rightarr, rightInv = CountInv(rightarr)
        finalarr, splitInv = CountSplitInv(leftarr, rightarr)
        #        print(leftInv, rightInv, splitInv)
        return finalarr, leftInv + rightInv + splitInv


print(CountInv(testarr)[1])
