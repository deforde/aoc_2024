#!python

import sys


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split('\n')
    data = [list(filter(None, line.split(' '))) for line in data]
    data = [
        sorted([int(subdata[i]) for subdata in data])
        for i in range(len(data[0]))
    ]
    data = [
        abs(data[0][i] - data[1][i])
        for i in range(len(data[0]))
    ]
    ans = sum(data)
    print(ans)


if __name__ == "__main__":
    main()
