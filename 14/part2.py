#!python

import sys
from pprint import pprint
from statistics import variance


def print_robots(robots, nx, ny):
    grid = []
    for _ in range(ny):
        row = ' ' * nx
        grid.append(row)
    for robot in robots:
        px, py, _, _ = robot
        if grid[py][px] == ' ':
            grid[py] = grid[py][:px] + '#' + grid[py][px + 1:]
    for y in range(ny):
        print(grid[y])
    print()


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()

    nx = int(sys.argv[2])
    ny = int(sys.argv[3])

    robots = []
    for line in data.split('\n'):
        pvtext = line.split(' ')

        ptext = pvtext[0].split('=')[1]
        px, py = ptext.split(',')
        px = int(px)
        py = int(py)

        vtext = pvtext[1].split('=')[1]
        vx, vy = vtext.split(',')
        vx = int(vx)
        vy = int(vy)

        robots.append((px, py, vx, vy))

    avg_xvar = 0
    avg_yvar = 0
    n = 0
    while True:
        for i, robot in enumerate(robots):
            px, py, vx, vy = robot
            px += vx
            py += vy
            while px < 0:
                px += nx
            while py < 0:
                py += ny
            px %= nx
            py %= ny
            robots[i] = (px, py, vx, vy)
        n += 1
        xvar = variance(robot[0] for robot in robots)
        yvar = variance(robot[1] for robot in robots)
        if xvar <= 0.75 * avg_xvar and yvar <= 0.75 * avg_yvar:
            # print_robots(robots, nx, ny)
            break
        avg_xvar += (xvar - avg_xvar) / n
        avg_yvar += (yvar - avg_yvar) / n
    print(n)


if __name__ == "__main__":
    main()

