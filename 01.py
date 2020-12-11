# 115/88 (not counted)
from sys import stdin
from itertools import product

data = list(map(int, stdin.read().strip().split('\n')))
w = len(data)

for i in data:
    if 2020 - i in data:
        print('A', i * (2020 - i))
        break
for i, j in product(range(w), range(w)):
    if 2020 - data[i] - data[j] in data:
        print('B', data[i] * data[j] * (2020 - data[i] - data[j]))
        break