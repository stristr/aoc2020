# 242/203
# 09:28/09:32
from sys import stdin

x, y = map(int, stdin.read().strip().split('\n'))

for n in range(20201227):
    if pow(7, n, 20201227) == x:
        print('a', pow(y, n, 20201227))
        break
