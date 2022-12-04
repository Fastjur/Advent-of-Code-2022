def fully_overlaps(a, b):
    return a[0] <= b[0] and a[1] >= b[1] or b[0] <= a[0] and b[1] >= a[1]


with open('input.txt') as f:
    lines = [[[int(i) for i in elf.split('-')] for elf in line.strip().split(',')] for line in f.readlines()]
    print(lines)
    pairs_fully_overlapping = 0
    for line in lines:
        overlaps = fully_overlaps(line[0], line[1])
        print(line, overlaps)
        if overlaps:
            pairs_fully_overlapping += 1
    print('Pairs fully overlapping:', pairs_fully_overlapping)