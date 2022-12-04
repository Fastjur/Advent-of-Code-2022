rock_points = 1
paper_points = 2
scissors_points = 3

draw_points = 3
win_points = 6

lose = 'X'
draw = 'Y'
win = 'Z'

opponent_rock = 'A'
opponent_paper = 'B'
opponent_scissors = 'C'


def get_lose(opponent):
    if opponent == opponent_rock:
        return scissors_points
    if opponent == opponent_paper:
        return rock_points
    if opponent == opponent_scissors:
        return paper_points


def get_draw(opponent):
    if opponent == opponent_rock:
        return rock_points
    if opponent == opponent_paper:
        return paper_points
    if opponent == opponent_scissors:
        return scissors_points


def get_win(opponent):
    if opponent == opponent_rock:
        return paper_points
    if opponent == opponent_paper:
        return scissors_points
    if opponent == opponent_scissors:
        return rock_points


def get_round_result(opponent, us):
    points = None

    if us == lose:
        points = get_lose(opponent)
    if us == win:
        points = get_win(opponent) + win_points
    if us == draw:
        points = get_draw(opponent) + draw_points

    if points is None:
        raise Exception('Invalid input')

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
