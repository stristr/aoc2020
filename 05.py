# 387/755
from sys import stdin
from functools import reduce

data = stdin.read().strip().split('\n')

rows = sorted(reduce(lambda x, c: 2 * x + (1 if c in ['B', 'R'] else 0), pattern, 0) for pattern in data)
print('a', rows[-1])
print('b', next(rows[i] + 1 for i in range(len(rows)) if rows[i+1] != rows[i] + 1))
