with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    print(lines)
    for line in lines:
        print()
        for i in range(14, len(line) + 1):
            substr = line[i-14:i]
            num_distinct = len(set(substr))
            if num_distinct == 14:
                print(substr, i)
                break
