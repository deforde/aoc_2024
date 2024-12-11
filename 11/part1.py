#!python

import sys


def run(data: list, n):
    for _ in range(n):
        i = 0
        while i < len(data):
            x = data[i]
            if x == 0:
                data[i] = 1
            elif len(str(x)) % 2 == 0:
                xs = str(x)
                a = int(xs[:len(xs) // 2])
                b = int(xs[len(xs) // 2:])
                data[i] = b
                data.insert(i, a)
                i += 1
            else:
                data[i] = x * 2024
            i += 1


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = [int(x) for x in data.split(' ')]
    run(data, int(sys.argv[2]))
    print(len(data))


if __name__ == "__main__":
    main()
