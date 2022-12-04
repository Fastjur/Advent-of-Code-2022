def overlaps_at_all(a, b):
    return a[0] <= b[1] and b[0] <= a[1] or b[0] <= a[1] and a[0] <= b[1]


with open('input.txt') as f:
    lines = [[[int(i) for i in elf.split('-')] for elf in line.strip().split(',')] for line in f.readlines()]
    print(lines)
    pairs_fully_overlapping = 0
    for line in lines:
        overlaps = overlaps_at_all(line[0], line[1])
        print(line, overlaps)
        if overlaps:
            pairs_fully_overlapping += 1
    print('Pairs overlapping at all:', pairs_fully_overlapping)