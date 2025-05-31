# test_case = [19,5,4,7,8,17,23,0]
import time
import functools

with open("problem15.9test2.txt", 'r') as input:
    lines = input.readlines()

lengths = {}
vertices = []
temp_list = []
for line in lines[1:]:
    contents = line.split("\n")
    contents = [*filter(lambda x: x != '', contents)]
    temp_list.extend(contents)

contents = [*map(lambda x: x.split(" "), temp_list)]
lengths = {f'{content[0]}-{content[1]}': int(content[2]) for content in contents}
for content in contents:
    lengths[f'{content[1]}-{content[0]}'] = int(content[2])
vertices = [*set([int(content[0]) for content in contents]).union(set([int(content[1]) for content in contents]))]


class Heap:
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
                elif self.lst[2*i - 1][1] > self.lst[i * 2][1]:
                    temp = self.lst[2*i - 1]
                    self.lst[2*i - 1] = self.lst[i * 2]
                    self.lst[i * 2] = temp
                i -= 1
        #print(f"output: {self.lst}")

    def insert(self, element):
        #print(f"input: {self.lst}")
        self.lst.append(element)
        self.size += 1
        self.swap(self.size)

    def extractmin(self):
        val = self.lst[0][0]
        del self.lst[0]
        self.size -= 1
        if self.size % 2 == 1:
            self.swap(self.size-1)
        else:
            self.swap(self.size)
        return val

    def delete(self, deleted):
        ix = self.lst.index(deleted)
        temp = self.lst[-1]
        self.lst[ix] = temp
        self.lst[-1] = deleted
        del self.lst[-1]
        self.size -= 1
        #self.swap(self.size)


def Prim(vertices, lengths):
    h = Heap()
    costs = {}
    T = {}
    s = vertices[1]
    X = [s]
    winner = {}
    for vertex in vertices:
        if lengths.get(f"{s}-{vertex}") is not None:
            costs[vertex] = lengths[f"{s}-{vertex}"]
            winner[vertex] = f"{s}-{vertex}"
        else:
            costs[vertex] = 999999999999
            winner[vertex] = ""
        h.insert((vertex, costs[vertex]))
    while h.size > 0:
        w = h.extractmin()
        X.append(w)
        T[w] = [winner[w], costs[w]]
        Y = set(vertices).difference(X)
        for y in Y:
            key = f"{w}-{y}"
            if lengths.get(key) is not None:
                if lengths[key] < costs[y]:
                    h.delete((y, costs[y]))
                    costs[y] = lengths[key]
                    winner[y] = key
                    h.insert((y, costs[y]))
    del T[s]
    total = functools.reduce(lambda a, b: a+b, [v[1] for k,v in T.items()])
    return total


start_time = time.time()
print(Prim(vertices=vertices, lengths=lengths))
print(time.time() - start_time, "seconds")

