# 203/125
# 19:11/1:18:12
from sys import stdin
from functools import reduce
from math import prod, sqrt

def parse(data):
    data = data.split('\n')
    dim = int(data[0].split(' ')[1][:-1])
    return dim, data[1:]

grids = list(map(parse, stdin.read().strip().split('\n\n')))

def rotate(grid):
    return [''.join(r) for r in zip(*grid[::-1])]

def flipX(grid):
    return [''.join(reversed(row)) for row in grid]

def flipY(grid):
    return list(reversed(grid))

def all_perms(grid):
    opts = [grid, flipX(grid), flipY(grid)]
    flippedX, flippedY = flipX(grid), flipY(grid)
    for _ in range(3):
        grid = rotate(grid)
        opts += [grid, flipX(grid), flipY(grid)]
    return opts

def rev(s):
    return ''.join(reversed(s))

def top(grid):
    return grid[0]

def bottom(grid):
    return grid[-1]

def left(grid):
    l = ''
    for i in range(len(grid)):
        l += grid[i][0]
    return l

def right(grid):
    r = ''
    for i in range(len(grid)):
        r += grid[i][-1]
    return r

def edges(grid):
    return set([grid[0], grid[-1], rev(grid[0]), rev(grid[-1]), left(grid), right(grid), rev(left(grid)), rev(right(grid))])

adj = {id: edges(grid) for id, grid in grids}

def possible_neighbors(id, edges):
    possibilities = []
    for neighbor_id, neighbor_edges in adj.items():
        if id == neighbor_id:
            continue
        matching = [edge for edge in neighbor_edges if edge in edges]
        if len(matching) > 0:
            assert len(matching) == 2
            possibilities.append((neighbor_id, matching[0]))
    return possibilities

neighbors = {id: possible_neighbors(id, edges) for id, edges in adj.items()}
print('a', prod(id for id, ns in neighbors.items() if len(ns) == 2))

size = int(sqrt(len(neighbors)))

def neighboring_ids(ns):
    return [id for id, edge in ns]

# Find IDs based on neighbors.
used, grid = [], []
while len(grid) < size:
    row = []
    grid.append(row)
    is_top = len(grid) == 1
    is_edge = is_top or len(grid) == size
    row.append(next(id for id, ns in neighbors.items() if id not in used and len(ns) == (2 if is_edge else 3) and (is_top or id in neighboring_ids(neighbors[grid[-2][0]]))))
    used.append(row[-1])
    while len(row) < size - 1:
        row.append(next(id for id, ns in neighbors.items() if id not in used and len(ns) == (3 if is_edge else 4) and row[-1] in neighboring_ids(ns) and (len(grid) < 2 or id in neighboring_ids(neighbors[grid[-2][len(row)]]))))
        used.append(row[-1])
    row.append(next(id for id, ns in neighbors.items() if id not in used and len(ns) == (2 if is_edge else 3) and row[-1] in neighboring_ids(ns) and (len(grid) < 2 or id in neighboring_ids(neighbors[grid[-2][len(row)]]))))
    used.append(row[-1])

# Find actual orientations based on IDs.
def fill_row(row):
    r = None
    if len(row) == 0:
        for orientation in all_perms(grids[grid[len(final_grid) - 1][0]]):
            if top(orientation) == bottom(final_grid[-2][0]):
                row.append(orientation)
                r = right(orientation)
                break
    else:
        r = right(row[-1])
    while len(row) < size:
        for orientation in all_perms(grids[grid[len(final_grid) - 1][len(row)]]):
            if r == left(orientation):
                r = right(orientation)
                row.append(orientation)
                break

grids = {id: grid for id, grid in grids}
for orientation in all_perms(grids[grid[0][0]]):
    r, b = right(orientation), bottom(orientation)
    if r in adj[grid[0][1]] and b in adj[grid[1][0]]:
        row = [orientation]
        break
assert row is not None
final_grid = [row]
fill_row(row)

while len(final_grid) < size:
    row = []
    final_grid.append(row)
    fill_row(row)

no_borders = list(map(lambda row: list(map(lambda grid: list(map(lambda s: s[1:-1], grid[1:-1])), row)), final_grid))
def merge(g1, g2):
    for i in range(len(g1)):
        g1[i] += g2[i]
    return g1
merged_rows = list(map(lambda row: reduce(merge, row), no_borders))
image = [r for chunk in merged_rows for r in chunk]

monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''.split('\n')[1:-1]
w, h = len(monster[0]), len(monster)
dots = [(x, y) for y in range(h) for x in range(w) if monster[y][x] == '#']
size = len(image)
hits = set()
found = False
for orientation in all_perms(image):
    for y in range(size - h):
        for x in range(size - w):
            if all(orientation[y+dy][x+dx] == '#' for dx, dy in dots):
                found = True
                for dx, dy in dots:
                    hits.add((x + dx, y + dy))
    if found:
        break

print('b', sum(1 for y in range(size) for x in range(size) if (x, y) not in hits and orientation[y][x] == '#'))
