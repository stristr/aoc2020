# 360/216
from sys import stdin

data = list(map(lambda x: x.split('\n'), stdin.read().strip().split('\n\n')))

print('a', sum(len(set(c for line in group for c in line)) for group in data))
print('b', sum(len(set(c for line in group for c in line if all(c in line for line in group))) for group in data))
