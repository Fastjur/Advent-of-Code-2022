import string

priorities = dict.fromkeys(string.ascii_lowercase) | dict.fromkeys(string.ascii_uppercase)
for i, key in enumerate(priorities):
    priorities[key] = i + 1

print(priorities)


def sort(str_array):
    return sorted(str_array, key=lambda x: priorities[x])


def strip_and_split(line):
    line = line.strip()
    return line
    # midway_index = len(line) // 2
    # # return [sort(line[:midway_index]), sort(line[midway_index:])]
    # return [line[:midway_index], line[midway_index:]]


def chunk(list_to_chunk, n):
    return [list_to_chunk[i:i + n] for i in range(0, len(list_to_chunk), n)]


with open('input.txt') as f:
    groups = chunk(f.readlines(), 3)
    groups = [[rucksack.strip() for rucksack in group] for group in groups]
    for i, group in enumerate(groups):
        print(f'Group {i + 1}')
        print(f'{group}\n')
    common_items = []
    for group in groups:
        common_items.append([item for item in group[0] if item in group[1] and item in group[2]][0])
    print(common_items)
    total_priority = 0
    for item in common_items:
        total_priority += priorities[item]
    print(total_priority)
