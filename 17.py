# 358/477
# 16:41/23:26
from sys import stdin
from itertools import product
from functools import reduce

data = list(map(list, stdin.read().strip().split('\n')))
h, w = len(data), len(data[0])

# [0]    -> [(-1), (1)]
# [0, 0] -> [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# ...
def neighbors(v):
    return [tuple([vv + d[i] for i, vv in enumerate(v)])
        for d in product(*[[-1, 0, 1]]*len(v)) if any(dd != 0 for dd in d)]

# Everything that might change.
def scope():
    return active.union(reduce(set.union, (set(neighbors(v)) for v in active)))

def play(active):
    keep = set()
    for v in scope():
        n = sum(1 for neighbor in neighbors(v) if neighbor in active)
        if v in active:
            if n in [2, 3]:
                keep.add(v)
        elif n == 3:
            keep.add(v)
    return keep

active = set((x, y, 0) for x, y in product(range(w), range(h)) if data[y][x] == '#')
for _ in range(6):
    active = play(active)
print('a', len(active))

active = set((x, y, 0, 0) for x, y in product(range(w), range(h)) if data[y][x] == '#')
for _ in range(6):
    active = play(active)
print('b', len(active))
