rock_points = 1
paper_points = 2
scissors_points = 3

draw_points = 3
win_points = 6

us_rock = 'X'
us_paper = 'Y'
us_scissors = 'Z'

opponent_rock = 'A'
opponent_paper = 'B'
opponent_scissors = 'C'


def get_round_result(opponent, us):
    points = 0

    if us == us_rock:
        points += rock_points
    if us == us_paper:
        points += paper_points
    if us == us_scissors:
        points += scissors_points

    if opponent == opponent_rock:
        if us == us_paper:
            points += win_points
        if us == us_rock:
            points += draw_points

    if opponent == opponent_paper:
        if us == us_scissors:
            points += win_points
        if us == us_paper:
            points += draw_points

    if opponent == opponent_scissors:
        if us == us_rock:
            points += win_points
        if us == us_scissors:
            points += draw_points

    return points


with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]
    print(lines)
    total_points = 0
    for line in lines:
        round_points = get_round_result(line[0], line[1])
        print(round_points)
        total_points += round_points
    print('Total points:', total_points)
