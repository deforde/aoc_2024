#!python

import sys


def check_seq(seq):
    dir = 'up' if seq[1] > seq[0] else 'down'
    for n in range(1, len(seq)):
        if dir == 'up':
            diff = seq[n] - seq[n - 1]
        else:
            diff = seq[n - 1] - seq[n]
        if diff < 1 or diff > 3:
            return False
    return True


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split('\n')
    data = [list(filter(None, line.split(' '))) for line in data]
    ans = 0
    for line in data:
        seq = [int(x) for x in line]
        if check_seq(seq):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
