import time

with open("problem14.6test3.txt", 'r') as infile:
    freqs = infile.read()
freqs = freqs.split("\n")[1:]
freqs.pop()
freqs = [*map(int, freqs)]


class HuffmanTree:
    def __init__(self, value):
        self.root = value
        self.compress = ""
        self.leaf = [None, None, None, self.root, self.compress]
        self.tree = [self.leaf]

    def merge(self, other):
        parent = self.root + other.root
        if self.root > other.root:
            left = other.root
            right = self.root
            self.leaf[4] = "1"
            other.leaf[4] = "0"
        else:
            left = self.root
            right = other.root
            self.leaf[4] = "0"
            other.leaf[4] = "1"
        self.root = parent
        other.root = parent
        self.leaf[2] = parent
        other.leaf[2] = parent
        parent_leaf = [left, right, None, parent, ""]
        for t in self.tree:
            if parent != t[2]:
                t[4] = ''.join((self.leaf[4], t[4]))

        for t in other.tree:
            if parent != t[2]:
                t[4] = ''.join((other.leaf[4], t[4]))
        temp = [parent_leaf]
        temp.extend(self.tree)
        self.tree = temp
        self.tree.extend(other.tree)
        self.leaf = parent_leaf


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


def HuffmanCoding(frequencies):
    tree_dict = {}
    print(frequencies)
    h = Heap()
    for i, frequency in enumerate(frequencies):
        if frequency in tree_dict.keys():
            ht = HuffmanTree(frequency + 1)
            tree_dict[frequency + 1] = ht
            h.insert((frequency+1, frequency+1))
        else:
            ht = HuffmanTree(frequency)
            tree_dict[frequency] = ht
            h.insert((frequency, frequency))
    while len(tree_dict) > 1:
        first_value = h.extractmin()
        second_value = h.extractmin()
        min_tree_1 = tree_dict[first_value]
        min_tree_2 = tree_dict[second_value]
        del tree_dict[first_value]
        del tree_dict[second_value]
        summation = min_tree_1.root + min_tree_2.root
        min_tree_1.merge(min_tree_2)
        i = i + 1
        h.insert((summation, summation))
        tree_dict[summation] = min_tree_1
    key = [k for k, v in tree_dict.items()][0]
    tree_list = tree_dict[key]
    final_codes = [(t[3], t[4]) for t in tree_list.tree if t[1] is None]
    return final_codes

start_time = time.time()
result_list = HuffmanCoding(freqs)
print(time.time() - start_time, "seconds")

len_list = [len(i[1]) for i in result_list]
print(min(len_list), max(len_list))

