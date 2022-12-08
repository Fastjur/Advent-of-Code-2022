def check_if_distinct(a, b, c, d):
    return a != b and a != c and a != d and b != c and b != d and c != d


with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    print(lines)
    for line in lines:
        for i in range(3, len(line)):
            if check_if_distinct(line[i - 3], line[i - 2], line[i - 1], line[i]):
                print(line[i-3], line[i-2], line[i-1], line[i], 'is distinct, char num:', i + 1)
                break
