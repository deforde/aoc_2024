#!python

import sys


def find_rules(rules, n):
    ret = []
    for rule in rules:
        if n in rule:
            ret.append(rule)
    return ret


def validate_update(update, rules):
    for i, n in enumerate(update):
        rel = find_rules(rules, n)
        for r in rel:
            if r[0] == n:
                x = r[1]
                if x in update and x not in update[i + 1:]:
                    return False
            else:
                x = r[0]
                if x in update and x not in update[:i]:
                    return False
    return True


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split("\n\n")
    rules = [
        [int(x) for x in line.split("|")]
        for line in data[0].split("\n")
    ]
    updates = [
        [int(x) for x in line.split(",")]
        for line in data[1].split("\n")
    ]

    ans = 0
    for update in updates:
        if validate_update(update, rules):
            ans += update[int(len(update) // 2)]
    print(ans)


if __name__ == "__main__":
    main()
