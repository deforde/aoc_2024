#!python

import sys
import re


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    matches = re.findall(r"mul\((\d+),(\d+)\)", data)
    ans = sum(int(x[0]) * int(x[1]) for x in matches)
    print(ans)


if __name__ == "__main__":
    main()
