# 638/378
from sys import stdin
from re import compile

def parse_lines(lines):
    # hcl:#6b5442 ... -> [('hcl', '#6b5442'), ...]
    return [(typ, v) for line in map(lambda x: map(lambda x: x.split(':'), x.split(' ')), lines.split('\n')) for typ, v in line]

data = list(map(parse_lines, stdin.read().strip().split('\n\n')))
# Rules for A
needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# Rules for B
hgt, hcl, pid = compile('^(\d+)(cm|in)$'), compile('^#[0-9a-f]{6}$'), compile('^\d{9}$')
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid(typ, v):
    if typ == 'byr':
        return 1920 <= int(v) <= 2002
    if typ == 'iyr':
        return 2010 <= int(v) <= 2020
    if typ == 'eyr':
        return 2020 <= int(v) <= 2030
    if typ == 'hgt':
        matches = hgt.match(v)
        if matches is None:
            return False
        n, u = matches.groups()
        return 150 <= int(n) <= 193 if u == 'cm' else 59 <= int(n) <= 76
    if typ == 'hcl':
        return hcl.match(v) is not None
    if typ == 'ecl':
        return v in ecl
    if typ == 'pid':
        return pid.match(v) is not None
    return True

a, b = 0, 0
for pp in data:
    if all(n in [typ for typ, _ in pp] for n in needed):
        a += 1
        if all(valid(typ, v) for typ, v in pp):
            b += 1

print('a', a)
print('b', b)
