# 281/319
# 09:41/23:37
from sys import stdin
from re import compile
from collections import defaultdict

data = stdin.read().strip().split('\n')
exp = compile('mem\[(\d+)\] = (\d+)')

mem = defaultdict(int)

def masked(mask, val):
    # &: 0 in mask overwrites 1
    # |: 1 in mask overwrites 0
    return val & int(mask.replace('X', '1'), 2) | int(mask.replace('X', '0'), 2)

def maskings(reg, mask):
    masks = ['']
    for c in mask:
        if c == '0':
            masks = [m + 'X' for m in masks]
        elif c == '1':
            masks = [m + '1' for m in masks]
        else:
            masks = [m + '0' for m in masks] + [m + '1' for m in masks]
    return [masked(m, reg) for m in masks]

mem_a, mem_b = defaultdict(int), defaultdict(int)
for line in data:
    if line.startswith('mask = '):
        mask = line.split(' = ')[1]
        continue
    reg, val = map(int, exp.match(line).groups())
    mem_a[reg] = masked(mask, val)
    for reg in maskings(reg, mask):
        mem_b[reg] = val
print('a', sum(val for val in mem_a.values()))
print('b', sum(val for val in mem_b.values()))
