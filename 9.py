# 603/658
from sys import stdin
from itertools import combinations

data = list(map(int, stdin.read().strip().split('\n')))
offset = 25

n = None
for i in range(offset, len(data) - offset):
    okay = False
    for x, y in combinations(set(data[i-offset:i]), 2):
        if x + y == data[i]:
            okay = True
            break
    if not okay:
        n = data[i]
        break

assert n is not None
print('a', n)

for i in range(2, len(data)):
    for j in range(0, len(data) - i):
        if sum(data[j:j+i]) == n:
            sl = data[j:j+i]
            print('b', min(sl) + max(sl))
            break
