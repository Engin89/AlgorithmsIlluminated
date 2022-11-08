# test_case = [19,5,4,7,8,17,23,0]
import time

with open("DijkstraTest2.txt", 'r') as input:
    lines = input.readlines()

lengths = {}
vertices = []
for line in lines:
    contents = line.split("\t")
    vertices.append(contents[0])
    for content in contents:
        content = content.replace('\n', '')
        if ',' in content:
            edge = contents[0] + '-' + content.split(',')[0]
            lengths[edge] = int(content.split(',')[1])


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


def FastDijkstra(vertices, start_point, lengths):
    X = []
    h = Heap()
    width = {}
    shortest_paths = {}
    for vertex in vertices:
        if vertex == start_point:
            width[vertex] = 0
            h.insert((vertex, width[vertex]))
        else:
            width[vertex] = 999999999999
            h.insert((vertex, width[vertex]))
    while h.size > 0:
        w = h.extractmin()
        X.append(w)
        shortest_paths[w] = width[w]
        Y = set(vertices).difference(X)
        for y in Y:
            key = f"{w}-{y}"
            if lengths.get(key) is not None:
                h.delete((y, width[y]))
                if width[y] > shortest_paths[w] + lengths[key]:
                    width[y] = shortest_paths[w] + lengths[key]
                h.insert((y, width[y]))
    return shortest_paths


start_time = time.time()
print(FastDijkstra(vertices=vertices, start_point='1', lengths=lengths)['197'])
print(time.time() - start_time, "seconds")

h = Heap()
for value in 2,4,3,5,7,6,1:
    h.insert((value, value))
print(h.extractmin())  # 1 = OK
h.insert((1,1))
print(h.extractmin())  # 2 = OK
h.insert((1,1))
print(h.extractmin())  # 4 = NOK. 3 expected.
print(h.extractmin())  # 4 = NOK. 3 expected.
h.insert((2,2))
print(h.extractmin())  # 4 = NOK. 3 expected.
print(h.extractmin())  # 4 = NOK. 3 expected.
print(h.extractmin())  # 4 = NOK. 3 expected.
