with open('input.txt') as f:
    lines = [int(line.strip()) if line != '\n' else None for line in f.readlines()]
    print(lines)
    calories = list()
    elf = 0
    highest = 0
    for i, line in enumerate(lines):
        if line is not None:
            print(i, line, calories)
            if len(calories) <= elf:
                calories.append(line)
            else:
                calories[elf] += line
        else:
            if calories[elf] > highest:
                highest = calories[elf]
            elf = elf + 1
    print(highest)
