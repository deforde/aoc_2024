#!python

import sys


def add_to_region(data, regions: list, a):
    adjacent_regions = set()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        b = a[0] + dx, a[1] + dy
        for i, region in enumerate(regions):
            if b in region and data[a[0]][a[1]] == data[b[0]][b[1]]:
                adjacent_regions.add(i)
    if adjacent_regions:
        new_region = []
        for i in adjacent_regions:
            new_region.extend(regions[i])
        adjacent_regions = sorted(adjacent_regions)[::-1]
        for i in adjacent_regions:
            regions.pop(i)
        new_region.append(a)
        regions.append(new_region)
    else:
        regions.append([a])


def get_regions(data):
    regions = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            p = x, y
            add_to_region(data, regions, p)
    return regions


def get_perimeter(region):
    perim = 0
    for a in region:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            b = a[0] + dx, a[1] + dy
            if b not in region:
                perim += 1
    return perim


def main():
    file = sys.argv[1]
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.read()
    data = data.split('\n')
    regions = get_regions(data)
    ans = 0
    for region in regions:
        perim = get_perimeter(region)
        ans += perim * len(region)
    print(ans)


if __name__ == "__main__":
    main()
