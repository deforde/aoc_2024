#!python

import sys
from pprint import pprint


def convert(data):
    ret = []
    file = True
    id = 0
    for x in data:
        if file:
            ret.extend([id] * int(x))
            id += 1
        else:
            ret.extend([None] * int(x))
        file = not file
    return ret


def compress(data):
    i = len(data) - 1
    while None in data[:i]:
        if data[i]:
            j = 0
            while j < i:
                if data[j] is None:
                    break
                j += 1
            data[j] = data[i]
            data[i] = None
        i -= 1


def checksum(data):
    sum = 0
    for i, x in enumerate(data):
        if x is None:
            break
        sum += i * x
    return sum


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = convert(data)
    compress(data)
    ans = checksum(data)
    print(ans)


if __name__ == "__main__":
    main()
