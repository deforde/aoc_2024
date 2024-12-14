#!python

import sys
from pprint import pprint


def print_robots(robots, nx, ny):
    grid = []
    for _ in range(ny):
        row = ' ' * nx
        grid.append(row)
    for robot in robots:
        px, py, _, _ = robot
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

    for n in range(100):
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

    # print_robots(robots, nx, ny)

    counts = [0, 0, 0, 0]
    for px, py, _, _ in robots:
        if px < nx // 2:
            if py < ny // 2:
                counts[0] += 1
            elif py > ny // 2:
                counts[1] += 1
        elif px > nx // 2:
            if py < ny // 2:
                counts[2] += 1
            elif py > ny // 2:
                counts[3] += 1

    ans = 1
    for count in counts:
        ans *= count

    print(ans)


if __name__ == "__main__":
    main()
