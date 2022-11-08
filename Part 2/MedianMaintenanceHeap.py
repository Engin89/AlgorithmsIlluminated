import numpy as np
import time


class minHeap:
    def __init__(self):
        self.size = 0
        self.lst = []

    def swap(self, a):
        if self.size == 1:
            return self.lst
        else:
            if a == 1:
                i = 1
            else:
                i = a // 2
            while i > 0:
                if i * 2 - 1 >= self.size:
                    break
                elif self.lst[i - 1][1] > self.lst[i * 2 - 1][1]:
                    temp = self.lst[i - 1]
                    self.lst[i - 1] = self.lst[i * 2 - 1]
                    self.lst[i * 2 - 1] = temp
                elif i * 2 >= self.size:
                    break
                elif self.lst[i - 1][1] > self.lst[i * 2][1]:
                    temp = self.lst[i - 1]
                    self.lst[i - 1] = self.lst[i * 2]
                    self.lst[i * 2] = temp
                elif self.lst[2 * i - 1][1] > self.lst[i * 2][1]:
                    temp = self.lst[2 * i - 1]
                    self.lst[2 * i - 1] = self.lst[i * 2]
                    self.lst[i * 2] = temp
                i -= 1
        # print(f"output: {self.lst}")

    def insert(self, element):
        # print(f"input: {self.lst}")
        self.lst.append(element)
        self.size += 1
        self.swap(self.size)

    def extractmin(self):
        val = self.lst[0][0]
        del self.lst[0]
        self.size -= 1
        if self.size % 2 == 1:
            self.swap(self.size - 1)
        else:
            self.swap(self.size)
        return val

    def findmin(self):
        return self.lst[0][0]

    def delete(self, deleted):
        ix = self.lst.index(deleted)
        temp = self.lst[-1]
        self.lst[ix] = temp
        self.lst[-1] = deleted
        del self.lst[-1]
        self.size -= 1
        self.swap(self.size)


class maxHeap:
    def __init__(self):
        self.size = 0
        self.lst = []

    def swap(self, a):
        if self.size == 1:
            return self.lst
        else:
            if a == 1:
                i = 1
            else:
                i = a // 2
            while i > 0:
                if i * 2 - 1 >= self.size:
                    break
                elif self.lst[i - 1][1] < self.lst[i * 2 - 1][1]:
                    temp = self.lst[i - 1]
                    self.lst[i - 1] = self.lst[i * 2 - 1]
                    self.lst[i * 2 - 1] = temp
                elif i * 2 >= self.size:
                    break
                elif self.lst[i - 1][1] < self.lst[i * 2][1]:
                    temp = self.lst[i - 1]
                    self.lst[i - 1] = self.lst[i * 2]
                    self.lst[i * 2] = temp
                elif self.lst[2 * i - 1][1] < self.lst[i * 2][1]:
                    temp = self.lst[2 * i - 1]
                    self.lst[2 * i - 1] = self.lst[i * 2]
                    self.lst[i * 2] = temp
                i -= 1
        # print(f"output: {self.lst}")

    def insert(self, element):
        # print(f"input: {self.lst}")
        self.lst.append(element)
        self.size += 1
        self.swap(self.size)

    def extractmax(self):
        val = self.lst[0][0]
        del self.lst[0]
        self.size -= 1
        if self.size % 2 == 1:
            self.swap(self.size - 1)
        else:
            self.swap(self.size)
        return val

    def findmax(self):
        return self.lst[0][0]

    def delete(self, deleted):
        ix = self.lst.index(deleted)
        temp = self.lst[-1]
        self.lst[ix] = temp
        self.lst[-1] = deleted
        del self.lst[-1]
        self.size -= 1
        self.swap(self.size)


# test_case = [6331,2793,1640,9290,225,625,6195,2303,5685,1354]


test_case = np.loadtxt("problem11.3.txt").tolist()

l = []
med_list = []

h1 = maxHeap()
h2 = minHeap()

start_time = time.time()
for x in test_case:
    if not l:
        h1.insert((x, x))
        h_max = h1.findmax()
        h_min = h_max
        med = x

    else:
        if h_max > x:
            h1.insert((x, x))
            h_max = h1.extractmax()
            h2.insert((h_max, h_max))

        else:
            h2.insert((x, x))
            h_min = h2.extractmin()
            h1.insert((h_min, h_min))

        if h1.size > h2.size:
            h_max = h1.extractmax()
            h2.insert((h_max, h_max))

        elif h1.size < h2.size:
            h_min = h2.extractmin()
            h1.insert((h_min, h_min))

        h_max = h1.findmax()
        h_min = h2.findmin()

        if h1.size >= h2.size:
            med = h_max
        else:
            med = h_min

    l.append(x)
    med_list.append(med)
print(sum(med_list))
print(time.time() - start_time, "seconds")
