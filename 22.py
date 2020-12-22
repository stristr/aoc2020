# 478/195
# 06:59/25:11
from sys import stdin
from collections import deque

p1, p2 = list(map(lambda deck: list(map(int, deck.split('\n')[1:])), stdin.read().strip().split('\n\n')))

def win(p1, p2):
    p1.rotate(-1)
    p1.append(p2.popleft())

def play(p1, p2, recursive=False):
    p1, p2, history = deque(p1), deque(p2), set()
    while p1 and p2:
        h = (tuple(p1), tuple(p2))
        if h in history:
            return (1, p1)
        history.add(h)
        if recursive and len(p1) > p1[0] and len(p2) > p2[0]:
            won, _ = play(list(p1)[1:p1[0]+1], list(p2)[1:p2[0]+1], recursive=True)
            if won == 1:
                win(p1, p2)
            else:
                win(p2, p1)
        elif p1[0] > p2[0]:
            win(p1, p2)
        else:
            win(p2, p1)
    return (1, p1) if p1 else (2, p2)

def score(deck):
    return sum((len(deck) - i) * n for i, n in enumerate(deck))

_, deck = play(p1, p2)
print('a', score(deck))
_, deck = play(p1, p2, recursive=True)
print('b', score(deck))
