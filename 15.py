# 889/324
# 12:59/13:55
from sys import stdin

data = list(map(int, stdin.read().strip().split(',')))
record = {x: (i, i) for i, x in enumerate(data)}
last, turn = data[-1], len(data)

def play():
    num = record[last][1] - record[last][0]
    record[num] = (record[num][1] if num in record else turn, turn)
    return num, turn + 1

while turn < 2020:
    last, turn = play()
print('a', last)
while turn < 30000000:
    last, turn = play()
print('b', last)
