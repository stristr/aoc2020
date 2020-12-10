# 3507/636
from sys import stdin
from collections import defaultdict

data = list(sorted(map(int, stdin.read().strip().split('\n'))))
data = [0] + data + [max(data) + 3]

d3 = sum(1 for i in range(0, len(data) - 1) if data[i+1] - data[i] == 3)
d1 = sum(1 for i in range(0, len(data) - 1) if data[i+1] - data[i] == 1)
print('a', d1 * d3)

paths = defaultdict(int, {0: 1})
for i in range(len(data)):
    for j in range(max(0, i - 3), i):
        paths[i] += paths[j] if data[i] - data[j] <= 3 else 0
print('b', paths[len(data) - 1])
