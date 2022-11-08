import numpy as np

test_cases = np.loadtxt("problem12.4test.txt").tolist()  #[-3, -1, 1, 2, 9, 11, 7, 6, 2]


targets = [i for i in range(-10000, 10001)]

my_dict = {}
in_scope_dict = {}

for target in targets:
    in_scope = []
    for test_case in test_cases:
        my_dict[test_case] = test_case
    for test_case in test_cases:
        y = target - my_dict[test_case]
        if my_dict.get(y) is not None and my_dict.get(y) != test_case:
            in_scope = 1
        if in_scope == 1:
            in_scope_dict[target] = in_scope
print(len(in_scope_dict.keys()))
