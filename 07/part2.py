#!python

import sys


def get_all_seqs(seqs, n, ops):
    if n == len(seqs[0]):
        return
    m = len(seqs)
    for i in range(m):
        for j, op in enumerate(ops):
            if j == len(ops) - 1:
                seqs[i].append(op)
            else:
                seqs.append(seqs[i][:] + [op])
    get_all_seqs(seqs, n, ops)


def check_seq(r, d, seqs):
    for seq in seqs:
        x = 0
        op = None
        for i, v in enumerate(d):
            if op == '+':
                x += int(v)
            elif op == '*':
                x *= int(v)
            elif op == '|':
                x = int(str(x) + v)
            else:
                x = int(v)
            if i < len(seq):
                op = seq[i]
        if r == x:
            return True
    return False


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split("\n")
    ans = 0
    for line in data:
        r = int(line.split(':')[0])
        d = list(filter(None, line.split(':')[1].split(' ')))
        seqs = [[]]
        get_all_seqs(seqs, len(d) - 1, ['+', '*', '|'])
        if check_seq(r, d, seqs):
            ans += r
    print(ans)


if __name__ == "__main__":
    main()

