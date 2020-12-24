# 574/336
# 14:08/22:35
from sys import stdin
from re import findall
from functools import reduce

data = list(map(lambda line: findall(r'e|se|sw|w|nw|ne', line), stdin.read().strip().split('\n')))
dirs = {
    1: {'e': (1, 0), 'w': (-1, 0), 'ne': (1, -1), 'se': (1, 1), 'nw': (0, -1), 'sw': (0, 1)},
    0: {'e': (1, 0), 'w': (-1, 0), 'ne': (0, -1), 'se': (0, 1), 'nw': (-1, -1), 'sw': (-1, 1)}
}

tiles = set()
for line in data:
    x, y = (0, 0)
    for ins in line:
        dx, dy = dirs[y%2][ins]
        x += dx
        y += dy
    if (x, y) in tiles:
        tiles.remove((x, y))
    else:
        tiles.add((x, y))

print('a', len(tiles))

def adjacencies(x, y):
    return set((x + dx, y + dy) for dx, dy in dirs[y%2].values())

def neighbors(x, y):
    return sum(1 for x, y in adjacencies(x, y) if (x, y) in tiles)

for _ in range(100):
    remove, add = set(), set()
    for x, y in tiles:
        n = neighbors(x, y)
        if n == 0 or n > 2:
            remove.add((x, y))
    for x, y, in reduce(set.union, (adjacencies(x, y) for x, y in tiles)):
        if (x, y) in tiles:
            continue
        if neighbors(x, y) == 2:
            add.add((x, y))
    tiles = tiles.union(add) - remove

print('b', len(tiles))
