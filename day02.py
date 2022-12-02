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
    
    #'A X': 4, #rock vs rock           1 + 3 = 4
    #'A Y': 8, #rock vs paper          2 + 6 = 8
    #'A Z': 3, #rock vs scissors       3 + 0 = 3

    #'B X': 1, #paper vs rock          1 + 0 = 1
    #'B Y': 5, #paper vs paper         2 + 3 = 5
    #'B Z': 9, #paper vs scissors      3 + 6 = 9

    #'C X': 7, #scissors vs rock       1 + 6 = 7
    #'C Y': 2, #scissors vs paper      2 + 0 = 2
    #'C Z': 6, #scissors vs scissors   3 + 3 = 6
}

def get_rounds():
    '''
        
    '''

    rounds = []
    with open('day02-input.txt') as f:
        rounds = f.read().splitlines()
    return rounds

def part_one():
    '''
        
    '''

    total_score = 0
    for round in get_rounds():
        moves = round.split(' ')
        total_score += scores[scores[round]] + scores[moves[1]]
        #total_score += scores[round] 

    return total_score

def part_two():
    '''
        
    '''
    
    return ''
    

if __name__ == "__main__":
    print(f"Day 2 part 1: {part_one()}")
    print(f"Day 2 part 2: {part_two()}")