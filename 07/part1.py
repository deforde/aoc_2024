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
        c = ''
        for i, v in enumerate(d):
            c += v + ')'
            if i < len(seq):
                c += seq[i]
        c = '(' * c.count(')') + c
        if r == eval(c):
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
        get_all_seqs(seqs, len(d) - 1, ['+', '*'])
        if check_seq(r, d, seqs):
            ans += r
    print(ans)


if __name__ == "__main__":
    main()
