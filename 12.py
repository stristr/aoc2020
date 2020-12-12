# 158/387
# 05:56/16:13
from sys import stdin

# E1, ... -> [('E', 1), ...]
data = list(map(lambda line: (line[0], int(line[1:])), stdin.read().strip().split('\n')))

bearings = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}

class Point:
    def __init__(self, val):
        self.val = val

    def d(self):
        return int(abs(self.val.real) + abs(self.val.imag))

def solve(nsew, ship, wp):
    """
    nsew: what responds to NSEW
    ship: what responds to F
    wp:   what rotates; what ship moves to
    """
    for ins, n in data:
        if ins in 'NSEW':
            nsew.val += bearings[ins]*n
        elif ins == 'F':
            ship.val += wp.val*n
        elif ins == 'L':
            wp.val *= 1j ** (n // 90)
        elif ins == 'R':
            wp.val /= 1j ** (n // 90)
    return ship.d()

ship, wp = Point(0), Point(1)
print('a', solve(ship, ship, wp))

ship, wp = Point(0), Point(10 + 1j)
print('b', solve(wp, ship, wp))
