#!python

import sys
import re


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", data)
    matches = [list(filter(None, x)) for x in matches]
    ans = 0
    enabled = True
    for match in matches:
        if match[0] == "don't()":
            enabled = False
        elif match[0] == "do()":
            enabled = True
        elif enabled:
            ans += int(match[0]) * int(match[1])
    print(ans)


if __name__ == "__main__":
    main()
