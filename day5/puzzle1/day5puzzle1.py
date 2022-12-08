import re
from pprint import pprint


def chunk(str_to_chunk, n):
    return [str_to_chunk[i:i + n] for i in range(0, len(str_to_chunk), n)]


with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]
    mid_idx = lines.index('')
    figure = [[chunk.strip() for chunk in chunk(line, 4)] for line in lines[:mid_idx]]
    pprint(figure)
    stacks = []
    for row in figure:
        for (i, crate) in enumerate(row):
            # print(i, crate)
            if (len(stacks) - 1) < i:
                stacks.append([])
            if len(crate) <= 0 or crate[0] != '[':
                continue
            stacks[i].append(crate[1])

    for stack in stacks:
        stack.reverse()

    pprint(stacks)
    moves = lines[mid_idx + 1:]
    pprint(moves)

    regex = r"move (\d+) from (\d+) to (\d+)"
    for move in moves:
        number, from_stack, to_stack = [int(m) for m in re.findall(regex, move)[0]]
        print(number, from_stack, to_stack)
        from_stack -= 1
        to_stack -= 1
        for i in range(number):
            stacks[to_stack].append(stacks[from_stack].pop())

    res = ''
    for stack in stacks:
        res += stack.pop()
    print("Final result:", res)
