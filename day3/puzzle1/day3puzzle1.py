import string

priorities = dict.fromkeys(string.ascii_lowercase) | dict.fromkeys(string.ascii_uppercase)
for i, key in enumerate(priorities):
    priorities[key] = i + 1

print(priorities)


def sort(str_array):
    return sorted(str_array, key=lambda x: priorities[x])


def strip_and_split(line):
    line = line.strip()
    midway_index = len(line) // 2
    return [sort(line[:midway_index]), sort(line[midway_index:])]


with open('input.txt') as f:
    lines = [strip_and_split(line) for line in f.readlines()]
    print(lines, '\n')
    common_items = []
    for line in lines:
        first_half = line[0]
        second_half = line[1]
        print(first_half)
        print(second_half, '\n')
        common_items.append([item for item in first_half if item in second_half][0])
    print(common_items)
    sum_of_priorities = sum([priorities[item] for item in common_items])
    print(sum_of_priorities)
