#!python

import sys


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()

    machines = []
    for block in data.split('\n\n'):
        lines = block.split('\n')

        axyvalues = lines[0].split(': ')[1].split(', ')
        xa = int(axyvalues[0][1:])
        ya = int(axyvalues[1][1:])

        bxyvalues = lines[1].split(': ')[1].split(', ')
        xb = int(bxyvalues[0][1:])
        yb = int(bxyvalues[1][1:])

        pxyvalues = lines[2].split(': ')[1].split(', ')
        xp = int(pxyvalues[0].split('=')[1]) + 10000000000000
        yp = int(pxyvalues[1].split('=')[1]) + 10000000000000

        machines.append((xa, ya, xb, yb, xp, yp))

    cost = 0
    for xa, ya, xb, yb, xp, yp in machines:
        a = (xp * yb - xb * yp) / (xa * yb - ya * xb)
        b = (yp - a * ya) / yb
        if a == int(a) and b == int(b) and a >= 0 and b >= 0:
            cost += int(a) * 3 + int(b) * 1

    print(cost)


if __name__ == "__main__":
    main()
