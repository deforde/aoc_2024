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
            k = i
            while data[k] == data[i]:
                k -= 1
            l = i - k

            j = 0
            m = 0
            n = None
            while j < i:
                if data[j] is None:
                    if n is None:
                        n = j
                    m += 1
                    if m == l:
                        break
                else:
                    m = 0
                    n = None
                j += 1

            if m == l and n is not None:
                data[n:n + l] = [data[i]] * l
                data[i - l + 1:i + 1] = [None] * l

            i -= l
        else:
            i -= 1

    i = len(data) - 1
    while i > 0:
        if data[i] is not None:
            break
        i -= 1
    data = data[:i + 1]


def checksum(data):
    sum = 0
    for i, x in enumerate(data):
        if x is not None:
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
