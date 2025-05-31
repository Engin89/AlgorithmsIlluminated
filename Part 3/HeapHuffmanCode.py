import heapq
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


def HuffmanCoding(frequencies):
    tree_dict = {}
    print(frequencies)
    h = []
    for frequency in frequencies:
        if frequency in tree_dict.keys():
            ht = HuffmanTree(frequency+1)
            tree_dict[frequency+1] = ht
            heapq.heappush(h, frequency+1)
        else:
            ht = HuffmanTree(frequency)
            tree_dict[frequency] = ht
            heapq.heappush(h, frequency)
    while len(tree_dict) > 1:
        first_value = heapq.heappop(h)
        second_value = heapq.heappop(h)
        min_tree_1 = tree_dict[first_value]
        min_tree_2 = tree_dict[second_value]
        del tree_dict[first_value]
        del tree_dict[second_value]
        summation = min_tree_1.root + min_tree_2.root
        min_tree_1.merge(min_tree_2)
        heapq.heappush(h, summation)
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

