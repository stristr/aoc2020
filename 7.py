# 259/259
from sys import stdin
from re import compile
from collections import deque, defaultdict

line_matcher = compile("(.*) bags contain (.*).$")
content_matcher = compile("(\d+) (.*) bags?")

def parse_content(line):
    # contain no other bags -> (0, None)
    if line.startswith('no'):
        return 0, None
    # 4 striped white bags ->  (4, "striped white")
    n, color = content_matcher.match(line).groups()
    return int(n), color

def parse_line(line):
    color, rest = line_matcher.match(line).groups()
    # dark plum bags contain 3 wavy teal bags -> ("dark plum", [(3, "wavy teal")])
    return color, list(map(parse_content, rest.split(', ')))

data = list(map(parse_line, stdin.read().strip().split('\n')))
parents = defaultdict(list)
children = defaultdict(list)

for color, contents in data:
    children[color] = contents
    for n, content_color in contents:
        parents[content_color].append(color)

# A: count unique ancestors
a = set()
q = deque(['shiny gold'])
while q:
    color = q.popleft()
    for parent in parents[color]:
        if parent not in a:
            a.add(parent)
            q.append(parent)
print('a', len(a))

# B: count total children
def price(color, num):
    if color is None:
        return 0
    return num + sum(price(child, n * num) for n, child in children[color])

print('b', price('shiny gold', 1) - 1)
