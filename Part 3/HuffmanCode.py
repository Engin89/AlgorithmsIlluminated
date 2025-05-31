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

def argmin(iterable):
    return min(enumerate(iterable), key=lambda x: x[1])


def HuffmanCoding(frequencies):
    tree_list = []
    print(frequencies)
    for frequency in frequencies:
        ht = HuffmanTree(frequency)
        tree_list.append(ht)
    while len(tree_list) > 1:
        first_value, first_index = argmin(frequencies)[1], argmin(frequencies)[0]
        min_tree_1 = tree_list[first_index]
        frequencies.pop(first_index)
        tree_list.pop(first_index)
        second_value, second_index = argmin(frequencies)[1], argmin(frequencies)[0]
        min_tree_2 = tree_list[second_index]
        frequencies.pop(second_index)
        tree_list.pop(second_index)
        summation = first_value + second_value
        min_tree_1.merge(min_tree_2)
        frequencies.append(summation)

        tree_list.append(min_tree_1)
    final_codes = [(t[3],t[4]) for t in tree_list[0].tree if t[1] is None]

    return final_codes


start_time = time.time()
result_list = HuffmanCoding(freqs)
print(time.time() - start_time, "seconds")
len_list = [len(i[1]) for i in result_list]
print(min(len_list), max(len_list))
