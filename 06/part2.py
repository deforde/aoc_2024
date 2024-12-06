#!python

import sys
from pprint import pprint
import copy


def next_pos(grid, coord):
    ch = grid[coord[0]][coord[1]]
    if '^' == ch:
        nx = coord[0] - 1
        ny = coord[1]
    elif '>' == ch:
        nx = coord[0]
        ny = coord[1] + 1
    elif 'v' == ch:
        nx = coord[0] + 1
        ny = coord[1]
    elif '<' == ch:
        nx = coord[0]
        ny = coord[1] - 1
    else:
        raise RuntimeError()
    return nx, ny


def turn(grid, coord):
    ch = grid[coord[0]][coord[1]]
    if '^' == ch:
        return '>'
    if '>' == ch:
        return 'v'
    if 'v' == ch:
        return '<'
    if '<' == ch:
        return '^'
    raise RuntimeError()


def init_pos(grid):
    for x, row in enumerate(grid):
        for y, ch in enumerate(row):
            if ch in ['^', '<', '>', 'v']:
                return x, y
    raise RuntimeError()


def get_empty_positions(grid):
    empty = []
    for x, row in enumerate(grid):
        for y, ch in enumerate(row):
            if '.' == ch:
                empty.append((x, y))
    return empty


def detect_loop(p, grid, record):
    ch = grid[p[0]][p[1]]
    if p in record:
        if ch in record[p]:
            return True
        record[p].append(ch)
    else:
        record[p] = [ch]
    return False


def solve(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    p = init_pos(grid)
    record = {}
    while True:
        if detect_loop(p, grid, record):
            return False
        np = next_pos(grid, p)
        if np[0] >= nrows or np[1] >= ncols or np[0] < 0 or np[1] < 0:
            return True
        nch = grid[np[0]][np[1]]
        if nch == '#':
            och = turn(grid, p)
            grid[p[0]][p[1]] = och
        else:
            grid[np[0]][np[1]] = grid[p[0]][p[1]]
            grid[p[0]][p[1]] = 'x'
            p = np


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        grid = f.read()
    grid = grid.split("\n")
    grid = [
        list(row)
        for row in grid
    ]
    ans = 0
    empty_positions = get_empty_positions(grid)
    for p in empty_positions:
        ngrid = copy.deepcopy(grid)
        ngrid[p[0]][p[1]] = '#'
        if not solve(ngrid):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
