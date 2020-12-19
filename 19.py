# 589/138
# 30:26/32:02
from sys import stdin

def parse_rule(line):
    n, rule = line.split(': ')
    if '"' in rule:
        # (1, "a")
        return int(n), rule[1:-1]
    rule = rule.split(' | ')
    # (2, [[1, 3], [3, 1]])
    return int(n), list(map(lambda s: list(map(int, s.split(' '))), rule))

data = stdin.read().strip().split('\n\n')
rules = {n: rule for n, rule in map(parse_rule, data[0].split('\n'))}
messages = data[1].split('\n')

def matches(msg, seq):
    # match iff we're at the end
    if not msg or not seq:
        return not msg and not seq
    n, rest = seq[0], seq[1:]
    if type(rules[n]) == str:
        return msg[0] == rules[n] and matches(msg[1:], rest)
    return any(matches(msg, branch + rest) for branch in rules[n])

print('a', sum(1 for msg in messages if matches(msg, [0])))

rules[8], rules[11] = [[42], [42, 8]], [[42, 31], [42, 11, 31]]
print('b', sum(1 for msg in messages if matches(msg, [0])))
