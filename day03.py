def get_rucksacks():
    '''
        Splits input into each rucksack
    '''

    rucksacks = []
    with open('day03-input.txt') as f:
        rucksacks = f.read().splitlines()
    return rucksacks

def part_one():
    '''
        Splits each rucksack into 2 compartments, finds the common item in the two compartments,
        then calculates the priorities and returns the sum
    '''

    both = []    
    for sack in get_rucksacks():
        compartments = [sack[:len(sack)//2], sack[len(sack)//2:]]
        both.append((set(compartments[0]) & set(compartments[1])).pop())

    return calculate_priorities(both)

def part_two():
    '''
        Groups the rucksacks into 3, finds the common item in each rucksack of the group,
        then calculates the priorities and returns the sum
    '''

    rucksacks = get_rucksacks()
    all_three = []
    for i in range(0, len(rucksacks), 3):
        all_three.append((set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2])).pop())

    return calculate_priorities(all_three)
    
def calculate_priorities(items):
    '''
        Converts each item in the supplied list to its priority, then returns the sum
    '''

    items = [ord(x)-64+26 if x.isupper() else ord(x)-96 for x in items]
    return sum(items)

if __name__ == "__main__":
    print(f"Day 3 part 1: {part_one()}")
    print(f"Day 3 part 2: {part_two()}")