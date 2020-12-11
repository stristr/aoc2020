# 927/475
from sys import stdin
from itertools import product

def parse_line(line):
    return list(line)

data = list(map(parse_line, stdin.read().strip().split('\n')))
h, w  = len(data), len(data[0])

deltas = [(dx, dy) for dx, dy in product([-1, 0, 1], [-1, 0, 1]) if not (dx == dy == 0)]

def bounded(x, y):
    return 0 <= x < w and 0 <= y < h

def neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in deltas if bounded(x + dx, y + dy)]

def visible(x, y):
    visible = []
    for dx, dy in deltas:
        sx, sy = dx, dy
        while bounded(x + sx, y + sy):
            if data[y + sy][x + sx] != '.':
                visible.append((x + sx, y + sy))
                break
            sx += dx
            sy += dy
    return visible

def shuffle(layout, neighbors=neighbors, max_occupants=4):
    new_layout = []
    for y in range(h):
        row = []
        new_layout.append(row)
        for x in range(w):
            c = layout[y][x]
            if c == 'L' and sum(1 for x, y in neighbors(x, y) if layout[y][x] == '#') == 0:
                row.append('#')
            elif c == '#' and sum(1 for x, y in neighbors(x, y) if layout[y][x] == '#') >= max_occupants:
                row.append('L')
            else:
                row.append(c)
    return new_layout

def shuffle_b(layout):
    return shuffle(layout, neighbors=visible, max_occupants=5)

def occupied(layout):
    return sum(1 for x, y in product(range(w), range(h)) if layout[y][x] == '#')

layout, new_layout = data.copy(), shuffle(data)
while layout != new_layout:
    layout, new_layout = new_layout, shuffle(new_layout)
print('a', occupied(layout))

layout, new_layout = data.copy(), shuffle_b(data)
while layout != new_layout:
    layout, new_layout = new_layout, shuffle_b(new_layout)
print('b', occupied(layout))
