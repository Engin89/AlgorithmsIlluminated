import numpy as np
import time

test_case = np.loadtxt("problem11.3.txt").tolist()  # [6331,2793,1640,9290,225,625,6195,2303,5685,1354]


class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = []
        self.tree = {}


class BinarySearchTree:
    def __init__(self):
        self.size = 0
        self.root = [None, None, None, None, None, None]
        self.tree = {None: self.root}
        self.root_key = None

    def insert(self, key, element):
        self.tree[None] = [None, None, None, None, self.size, None]
        y = [None, None, None, None, None, None]
        x = self.root.copy()
        self.size += 1
        right_size = 0
        left_size = 0
        self.tree[key] = [element, y[0], None, None, 1, key]
        while x[0] is not None:
            y = x.copy()
            if element < x[0]:
                x = self.tree.get(x[2])
                left_size += 1
                self.tree[x[5]][4] += 1
            else:
                x = self.tree.get(x[3])
                right_size += 1
                self.tree[x[5]][4] += 1
        self.tree[self.root_key][4] = self.size
        if y[0] is None:
            self.root = self.tree[key]
            self.root_key = key
        elif element < y[0]:
            self.tree[y[5]][2] = key
            self.tree[key][1] = y[5]
        else:
            self.tree[y[5]][3] = key
            self.tree[key][1] = y[5]
        del self.tree[None]

    def select(self, rank, x):
        self.tree[None] = [None, None, None, None, 0, None]
        left = self.tree[x[2]][4]
        num = self.tree[x[5]][4]
        if left > rank:
            x = self.tree[x[2]]
            del self.tree[None]
            return self.select(rank, x)
        elif left < rank:
            x = self.tree[x[3]]
            del self.tree[None]
            return self.select(rank - left - 1, x)
        else:
            return x[0]


bst = BinarySearchTree()

l = []
start_time = time.time()
for i, j in enumerate(test_case, 1):
    bst.insert(i, j)
    if bst.size % 2 == 0:
        median = (bst.select(bst.size / 2 - 1, bst.root))
    else:
        median = (bst.select((bst.size - 1) / 2, bst.root))
    l.append(median)
print(sum(l))
print(time.time() - start_time, "seconds")
