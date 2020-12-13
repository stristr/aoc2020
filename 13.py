# 345/183
# 05:37/20:46
from sys import stdin
from math import prod

data = stdin.read().strip().split('\n')
n = int(data[0])
buses = [(int(p) - r, int(p)) for r, p in enumerate(data[1].split(',')) if p != 'x']
id, time = min([(p, p * (n // p) + p) for _, p in buses], key=lambda t: t[1])
print('a', id * (time - n))
lcm = prod(p for _, p in buses)
# Chinese remainder theorem:
#   r is the remainder
#   pow(lcm // p, p - 2, p) is the mod p inverse of lcm // p
#   (This works because all the p are prime.)
print('b', sum(r * lcm // p * pow(lcm // p, p - 2, p) for r, p in buses) % lcm)
