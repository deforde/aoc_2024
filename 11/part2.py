#!python

import sys


def update_count(x, n, data):
    found = False
    for i, p in enumerate(data):
        if p[0] == x:
            data[i] = data[i][0], data[i][1] + n
            found = True
    if not found:
        data.append((x, n))


def compress(data: list):
    ndata = []
    for x, n in data:
        update_count(x, n, ndata)
    return ndata


def run(data: list, n):
    data = compress(data)

    if n == 0:
        count = 0
        for _, m in data:
            count += m
        return count

    i = 0
    while i < len(data):
        x = data[i][0]
        if x == 0:
            data[i] = 1, data[i][1]
        elif len(str(x)) % 2 == 0:
            xs = str(x)
            a = int(xs[:len(xs) // 2])
            b = int(xs[len(xs) // 2:])
            data[i] = b, data[i][1]
            data.insert(i, (a, data[i][1]))
            i += 1
        else:
            data[i] = x * 2024, data[i][1]
        i += 1

    return run(data, n - 1)


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = [(int(x), 1) for x in data.split(' ')]
    count = run(data, int(sys.argv[2]))
    print(count)


if __name__ == "__main__":
    main()
