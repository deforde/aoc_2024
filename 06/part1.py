#!python

import sys
from pprint import pprint


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


def solve(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    p = init_pos(grid)
    while True:
        np = next_pos(grid, p)
        if np[0] >= nrows or np[1] >= ncols or np[0] < 0 or np[1] < 0:
            return sum(row.count('x') for row in grid) + 1
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
    print(solve(grid))


if __name__ == "__main__":
    main()
