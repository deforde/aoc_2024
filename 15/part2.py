#!python

import sys
from copy import deepcopy


def scale_grid(grid):
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[0]):
            ch = grid[i][j]
            if ch in ['#', '.']:
                grid[i].insert(j, ch)
                j += 1
            elif ch == 'O':
                grid[i].insert(j, '[')
                j += 1
                grid[i][j] = ']'
            elif ch == '@':
                grid[i].insert(j, '@')
                j += 1
                grid[i][j] = '.'
            j += 1
        i += 1


def do_move(p, move):
    if move == '^':
        return p[0] - 1, p[1]
    if move == '>':
        return p[0], p[1] + 1
    if move == 'v':
        return p[0] + 1, p[1]
    if move == '<':
        return p[0], p[1] - 1
    raise RuntimeError()


def can_move_to(grid, np, move, aux_moves):
    if grid[np[0]][np[1]] == '.':
        return True
    if grid[np[0]][np[1]] in ['[', ']']:
        if grid[np[0]][np[1]] == ']' and move == '>':
            return True
        if grid[np[0]][np[1]] == '[' and move == '<':
            return True
        ops = [np]
        if grid[np[0]][np[1]] == '[':
            ops.append((np[0], np[1] + 1))
        else:
            ops.append((np[0], np[1] - 1))
        bps = [do_move(op, move) for op in ops]
        valid = True
        this_aux_moves = []
        for op, bp in zip(ops, bps):
            if not can_move_to(grid, bp, move, aux_moves):
                valid = False
                break
            this_aux_moves.append((op, bp))
        if valid:
            aux_moves.extend(this_aux_moves)
            return True
    return False


def print_grid(grid):
    for row in grid:
        print(row)
    print()


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()

    blocks = data.split('\n\n')

    grid = blocks[0].split('\n')
    grid = [
        list(row)
        for row in grid
    ]
    moves = blocks[1]
    moves = moves.replace('\n', '')

    # print_grid(grid)
    scale_grid(grid)
    # print_grid(grid)

    p = 0, 0
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == '@':
                p = i, j
                break

    for move in moves:
        np = do_move(p, move)
        aux_moves = []
        if can_move_to(grid, np, move, aux_moves):
            ngrid = deepcopy(grid)
            for aux_move in aux_moves:
                a, b = aux_move
                ngrid[b[0]][b[1]] = grid[a[0]][a[1]]
                if a not in [x[1] for x in aux_moves]:
                    ngrid[a[0]][a[1]] = '.'
            ngrid[np[0]][np[1]] = '@'
            ngrid[p[0]][p[1]] = '.'
            grid = ngrid
            p = np
        # print_grid(grid)

    box_coords = []
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == '[':
                box_coords.append(j + 100 * i)

    ans = sum(box_coords)
    print(ans)


if __name__ == "__main__":
    main()
