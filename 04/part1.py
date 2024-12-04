#!python

import sys


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split("\n")
    nrows = len(data)
    ncols = len(data[0])

    horizontals = data

    verticals = []
    for col in range(ncols):
        vertical = ""
        for row in range(nrows):
            vertical += data[row][col]
        verticals.append(vertical)

    wediags = []
    for base_row in range(nrows):
        row = base_row
        col = 0
        wediag = ""
        while row < nrows and col < ncols:
            wediag += data[row][col]
            row += 1
            col += 1
        wediags.append(wediag)
    for base_col in range(1, ncols):
        row = 0
        col = base_col
        wediag = ""
        while row < nrows and col < ncols:
            wediag += data[row][col]
            row += 1
            col += 1
        wediags.append(wediag)

    ewdiags = []
    for base_row in range(nrows):
        row = base_row
        col = ncols - 1
        ewdiag = ""
        while row < nrows and col >= 0:
            ewdiag += data[row][col]
            row += 1
            col -= 1
        ewdiags.append(ewdiag)
    for base_col in range(0, ncols - 1):
        row = 0
        col = base_col
        ewdiag = ""
        while row < nrows and col >= 0:
            ewdiag += data[row][col]
            row += 1
            col -= 1
        ewdiags.append(ewdiag)

    dataset = horizontals + verticals + wediags + ewdiags

    ans = 0
    for string in dataset:
        ans += string.count("XMAS")
        ans += string.count("SAMX")
    print(ans)


if __name__ == "__main__":
    main()
