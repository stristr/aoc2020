# 786/641
from sys import stdin
from re import compile

exp = compile('(\w+) ([+-]\d+)')

def parse_line(line):
    cmd, n = exp.match(line).groups()
    return cmd, int(n)

data = list(map(parse_line, stdin.read().strip().split('\n')))

class VM:
    def __init__(self, ins, autorun=True):
        self.reset(ins, autorun=autorun)

    def reset(self, ins, autorun=True, acc=0):
        # Instructions
        self.ins = ins
        # Accumulator
        self.acc = acc
        # Instruction pointer
        self.ptr = 0
        # Currently running
        self.running = True
        # Indices we've seen
        self.seen = set()
        if autorun:
            self.run()

    def run(self):
        while True:
            if self.ptr in self.seen:
                return
            elif self.ptr < 0 or self.ptr >= len(self.ins):
                self.running = False
                return
            self.seen.add(self.ptr)
            cmd, n = self.ins[self.ptr]
            if cmd == 'jmp':
                self.ptr += n - 1
            elif cmd == 'acc':
                self.acc += n
            else:
                assert cmd == 'nop'
            self.ptr += 1

m = VM(data)
print('a', m.acc)

for i in range(len(data)):
    cmd, n = data[i]
    m.reset(data[:i] + [('jmp' if cmd == 'nop' else 'nop' if cmd == 'jmp' else cmd, n)] + data[i+1:])
    if not m.running:
        print('b', m.acc)
