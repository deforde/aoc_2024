#!python

import sys


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
    if grid[np[0]][np[1]] == 'O':
        bp = do_move(np, move)
        if can_move_to(grid, bp, move, aux_moves):
            aux_moves.append((np, bp))
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
            for aux_move in aux_moves:
                a, b = aux_move
                grid[b[0]][b[1]] = 'O'
                grid[a[0]][a[1]] = '.'
            grid[np[0]][np[1]] = '@'
            grid[p[0]][p[1]] = '.'
            p = np
        # print_grid(grid)

    box_coords = []
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == 'O':
                box_coords.append(j + 100 * i)

    ans = sum(box_coords)
    print(ans)


if __name__ == "__main__":
    main()
