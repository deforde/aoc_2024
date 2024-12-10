#!python

import sys


def get_all_trailheads(data):
    ths = []
    for x, row in enumerate(data):
        for y, p in enumerate(row):
            if 0 == p:
                ths.append((x, y))
    return ths


def walk_paths(data, paths):
    changed = False
    n = len(paths)
    for i in range(n):
        path = paths[i]
        p = path[-1]
        valid_nps = []
        a = data[p[0]][p[1]]
        for dx, dy in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            q = p[0] + dx, p[1] + dy
            if q[0] < 0 or q[0] >= len(data) or q[1] < 0 or q[1] >= len(data[0]):
                continue
            b = data[q[0]][q[1]]
            if a + 1 == b:
                valid_nps.append(q)
        for j, np in enumerate(valid_nps):
            changed = True
            if j == len(valid_nps) - 1:
                path.append(np)
            else:
                cp = path[:]
                cp.append(np)
                paths.append(cp)
    if not changed:
        return
    walk_paths(data, paths)


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split('\n')
    data = [
        [int(x) for x in row]
        for row in data
    ]
    ans = 0
    ths = get_all_trailheads(data)
    for th in ths:
        paths = [[th]]
        walk_paths(data, paths)
        paths = list(filter(lambda path: 9 == data[path[-1][0]][path[-1][1]], paths))
        ans += len(paths)
    print(ans)


if __name__ == "__main__":
    main()
