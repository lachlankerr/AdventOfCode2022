def get_elves():
    '''
        Splits input into each individual elf
    '''

    elves = []
    with open('day01-input.txt') as f:
        elves = f.read().split('\n\n')
    return elves

def get_elves_calories():
    '''
        Converts each elf into the sum of all their calories
    '''

    return sorted([sum(list(map(int, elf.splitlines()))) for elf in get_elves()])

def part_one():
    '''
        Gets the most calories a single elf is carrying
    '''

    return get_elves_calories().pop()

def part_two():
    '''
        Gets the sum of the top 3 most calories the elves are carrying
    '''
    
    return sum(get_elves_calories()[-3:])

if __name__ == "__main__":
    print(f"Day 1 part 1: {part_one()}")
    print(f"Day 1 part 2: {part_two()}")