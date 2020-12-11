# 368/516
from sys import stdin
from re import compile

pattern = compile('(\d+)-(\d+) (\w): (\w+)')

def parse_line(line):
    least, most, c, pwd = pattern.match(line).groups()
    return int(least), int(most), c, pwd

data = list(map(parse_line, stdin.read().strip().split('\n')))
print('A', sum(1 for least, most, c, pwd in data if least <= pwd.count(c) <= most))
print('B', sum(1 for least, most, c, pwd in data if (pwd[least-1] == c) ^ (pwd[most-1] == c)))
