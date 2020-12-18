# 417/253
# 15:49/20:00
from sys import stdin
from re import sub, split

data = stdin.read().strip().split('\n')

def no_parens(line, reducer):
    """Reduce unnested parens until none are left."""
    while '(' in line:
        line = sub(r'(\([^\(\)]+\))', lambda m: reducer(m.group(0)[1:-1]), line)
    return line

def calc_a(line):
    assert '(' not in line
    ns = list(map(int, split(r' [+*] ', line)))
    ops = split('\s?\d+\s?', line)
    a = ns[0]
    for i in range(1, len(ns)):
        a = a + ns[i] if ops[i] == '+' else a * ns[i]
    return str(a)

def calc_b(line):
    assert '(' not in line
    while '+' in line:
        line = sub(r'(\d+ \+ \d+)', lambda m: calc_a(m.group(0)), line)
    return calc_a(line)

print('a', sum(int(calc_a(no_parens(line, reducer=calc_a))) for line in data))
print('b', sum(int(calc_b(no_parens(line, reducer=calc_b))) for line in data))
