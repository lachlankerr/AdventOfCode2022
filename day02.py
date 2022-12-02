scores = {
    'A': 1, #rock
    'B': 2, #paper
    'C': 3, #scissors

    'X': 1, #rock
    'Y': 2, #paper
    'Z': 3, #scissors

    'L': 0, #lose
    'D': 3, #draw
    'W': 6, #win

    'A X': 'D', #rock vs rock           1 + 3 = 4
    'A Y': 'W', #rock vs paper          2 + 6 = 8
    'A Z': 'L', #rock vs scissors       3 + 0 = 3

    'B X': 'L', #paper vs rock          1 + 0 = 1
    'B Y': 'D', #paper vs paper         2 + 3 = 5
    'B Z': 'W', #paper vs scissors      3 + 6 = 9

    'C X': 'W', #scissors vs rock       1 + 6 = 7
    'C Y': 'L', #scissors vs paper      2 + 0 = 2
    'C Z': 'D', #scissors vs scissors   3 + 3 = 6
}

def get_rounds():
    '''
        Splits input into each round
    '''

    rounds = []
    with open('day02-input.txt') as f:
        rounds = f.read().splitlines()
    return rounds

def part_one():
    '''
        Gets total score when following the strategy guide
    '''

    total_score = 0
    for round in get_rounds():
        moves = round.split(' ')
        total_score += scores[scores[round]] + scores[moves[1]]

    return total_score

def part_two():
    '''
        Gets total score when following the proper strategy guide
    '''

    scores['X'] = 'L'
    scores['Y'] = 'D'
    scores['Z'] = 'W'

    scores['A X'] = 'C' # lose against rock = scissors
    scores['A Y'] = 'A' # draw against rock = rock
    scores['A Z'] = 'B' # win against rock = paper

    scores['B X'] = 'A' # lose against paper = rock
    scores['B Y'] = 'B' # draw against paper = paper
    scores['B Z'] = 'C' # win against paper = scissors

    scores['C X'] = 'B' # lose against scissors = paper
    scores['C Y'] = 'C' # draw against scissors = scissors
    scores['C Z'] = 'A' # win against scissors = rock

    total_score = 0
    for round in get_rounds():
        moves = round.split(' ')
        total_score += scores[scores[round]] + scores[scores[moves[1]]]

    return total_score
    

if __name__ == "__main__":
    print(f"Day 2 part 1: {part_one()}")
    print(f"Day 2 part 2: {part_two()}")