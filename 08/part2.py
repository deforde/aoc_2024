#!python

import sys
from pprint import pprint


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split("\n")
    nrows = len(data)
    ncols = len(data[0])

    antinodes = set()

    for ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        ps = []
        for x, row in enumerate(data):
            for y, v in enumerate(row):
                if v == ch:
                    ps.append((x, y))
        for i in range(len(ps) - 1):
            for j in range(1, len(ps)):
                a = ps[i]
                b = ps[j]
                antinodes.add(a)
                antinodes.add(b)
                ab = b[0] - a[0], b[1] - a[1]
                m = 2
                while True:
                    c = a[0] + m * ab[0], a[1] + m * ab[1]
                    if c[0] >= 0 and c[0] < nrows and c[1] >= 0 and c[1] < ncols and ch != data[c[0]][c[1]]:
                        antinodes.add(c)
                    else:
                        break
                    m += 1
                m = 2
                while True:
                    d = b[0] - m * ab[0], b[1] - m * ab[1]
                    if d[0] >= 0 and d[0] < nrows and d[1] >= 0 and d[1] < ncols and ch != data[d[0]][d[1]]:
                        antinodes.add(d)
                    else:
                        break
                    m += 1

    # for x, y in antinodes:
    #     if data[x][y] == '.':
    #         data[x] = data[x][:y] + '#' + data[x][y + 1:]
    # pprint(data)

    print(len(antinodes))


if __name__ == "__main__":
    main()
