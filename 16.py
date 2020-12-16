# 249/180
# 08:44/24:37
from sys import stdin
from math import prod

constraints, my_ticket, nearby_tickets = map(lambda x: x.split('\n'), stdin.read().strip().split('\n\n'))
rules = {}
for line in constraints:
    label, opts = line.split(': ')
    rules[label] = list(map(lambda opt: list(map(int, opt.split('-'))), opts.split(' or ')))
my_ticket = list(map(int, my_ticket[1].split(',')))
tickets = [list(map(int, line.split(','))) for line in nearby_tickets[1:]]
print('a', sum(i for ticket in tickets for i in ticket if all(
    not m <= i <= M for label, opts in rules.items() for [m, M] in opts)))

valid_tickets = [ticket for ticket in tickets if all(
    any(m <= i <= M for label, opts in rules.items() for [m, M] in opts) for i in ticket
)]

candidates = {
    i: [label for label, opts in rules.items() if all(
        any(m <= t[i] <= M for [m, M] in opts) for t in valid_tickets)]
    for i in range(len(my_ticket))
}

translations = {
    i: labels[0] for i, labels in candidates.items() if len(labels) == 1
}

while candidates:
    for i, opts in candidates.items():
        candidates[i] = [opt for opt in opts if opt not in translations.values()]
        if len(candidates[i]) == 1:
            translations[i] = candidates[i][0]
    candidates = {i: labels for i, labels in candidates.items() if len(labels) > 1}

print('b', prod(x for i, x in enumerate(my_ticket) if translations[i].startswith('departure')))
