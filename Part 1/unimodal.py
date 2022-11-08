testarr = [1,3,6,4,2,0]


def findMax(arr):
    end = len(arr)
    if end == 1:
        return arr[0]
    elif end == 0:
        return arr
    else:
        mid = int(end / 2)
        leftarr = arr[:mid]
        rightarr = arr[mid:]
        leftarr = findMax(leftarr)
        rightarr = findMax(rightarr)
        maxElement = compare(leftarr, rightarr)
        return maxElement


def compare(left, right):
    combinedArr = [left, right]
    if left > right:
        maxElement = left
    else:
        maxElement = combinedArr[-1]
    return maxElement


print(findMax(testarr))
