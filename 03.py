# 332/117
from sys import stdin

data = list(map(list, stdin.read().strip().split('\n')))
h, w = len(data), len(data[0])

def run(dx, dy):
    x, y = 0, 0
    a = 0
    while y < h - 1:
        x, y = (x + dx) % w, y + dy
        if data[y][x] == '#':
            a += 1
    return a

print('a', run(3, 1))
print('b', run(1, 1) * run(3, 1) * run(5, 1) * run(7, 1) * run(1, 2))
