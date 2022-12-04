with open('input.txt') as f:
    lines = [int(line.strip()) if line != '\n' else None for line in f.readlines()]
    print(lines)
    calories = list()
    elf = 0
    for i, line in enumerate(lines):
        if line is not None:
            print(i, line, calories)
            if len(calories) <= elf:
                calories.append(line)
            else:
                calories[elf] += line
        else:
            elf = elf + 1
    calories.sort(reverse=True)
    print(calories[0] + calories[1] + calories[2])
