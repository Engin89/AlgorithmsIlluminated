testarr = [54044, 14108, 79294, 29649, 25260, 60660, 2995, 53777, 49689, 9083]


def merge(left, right):
    n = len(left) + len(right)
    sortedArr = []
    for k in range(0, n):
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                sortedArr.append(left.pop(0))
            else:
                sortedArr.append(right.pop(0))
        elif len(left) == 0 and len(right) > 0 and len(sortedArr) < n:
            sortedArr.extend(right)
        elif len(right) == 0 and len(left) > 0 and len(sortedArr) < n:
            sortedArr.extend(left)
    return sortedArr


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    end = len(arr)
    mid = int(end / 2)
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    leftarr = mergesort(leftarr)
    rightarr = mergesort(rightarr)
    return merge(leftarr, rightarr)


print(mergesort(testarr))
