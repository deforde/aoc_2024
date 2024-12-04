#!python

import sys


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split("\n")
    nrows = len(data)
    ncols = len(data[0])

    ans = 0

    for base_row in range(nrows - 2):
        for base_col in range(ncols - 2):
            diags = []

            diag = ""
            row = base_row
            col = base_col
            while row < base_row + 3 and col < base_col + 3:
                diag += data[row][col]
                row += 1
                col += 1
            diags.append(diag)

            diag = ""
            row = base_row
            col = base_col + 2
            while row < base_row + 3 and col >= base_col:
                diag += data[row][col]
                row += 1
                col -= 1
            diags.append(diag)

            if all(diag in ["MAS", "SAM"] for diag in diags):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
