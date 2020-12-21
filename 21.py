# 98/91
# 11:19/15:26
from sys import stdin
from functools import reduce

def parse_line(line):
    l, r = line.split(' (')
    return l.split(' '), r[9:-1].split(', ')

data = list(map(parse_line, stdin.read().strip().split('\n')))
allergens = set(a for _, allergens in data for a in allergens)
candidates = {
    a: list(reduce(set.intersection, [set(a for a in ing) for ing, allergens in data if a in allergens])) for a in allergens
}
all_possible = reduce(set.union, map(set, candidates.values()))

print('a', sum(1 for ing, _ in data for a in ing if not a in all_possible))

culprits = {
    a: opts[0] for a, opts in candidates.items() if len(opts) == 1
}

while candidates:
    for a, opts in candidates.items():
        candidates[a] = [opt for opt in opts if opt not in culprits.values()]
        if len(candidates[a]) == 1:
            culprits[a] = candidates[a][0]
    candidates = {a: opts for a, opts in candidates.items() if a not in culprits}
print('b', ','.join(v for k, v in sorted(culprits.items(), key=lambda x: x[0])))
