# 960/164
# 28:58/45:25
from sys import stdin
from collections import deque

ns = list(map(int, list(stdin.read().strip())))

cups = deque(ns)
for _ in range(100):
    current, dest = cups[0], cups[0] - 1
    cups.rotate(-1)
    picked = []
    for _ in range(3):
        picked.append(cups.popleft())
    dest = current - 1
    while dest in picked or dest == 0:
        dest = dest - 1 if dest > 0 else 9
    cups.rotate(-cups.index(dest)-1)
    for d in picked:
        cups.append(d)
    cups.rotate(8-cups.index(current))
cups.rotate(9-cups.index(1))
print('a', ''.join(map(str, list(cups)[1:])))

class Node:
    def __init__(self, v):
        self.v = v
    
    def insert_after(self, node):
        node.next = self

ns += list(range(10, 1000001))
nodes = {v: Node(v) for v in ns}
for i, l in enumerate(ns):
    nodes[l].next = nodes[ns[i + 1] if i < 999999 else 1]

head = nodes[ns[0]]
for _ in range(10000000):
    current, dest, picked = head.v, head.v - 1, [head.next, head.next.next, head.next.next.next]
    picked_values = [node.v for node in picked]
    picked[-1].next.insert_after(head)
    while dest in picked_values or dest == 0:
        dest = dest - 1 if dest > 0 else 1000000
    nodes[dest].next.insert_after(picked[-1])
    picked[0].insert_after(nodes[dest])
    head = head.next
print('b', nodes[1].next.v * nodes[1].next.next.v)
