import re

def get_pairs():
    '''
        Splits input into pairs of section assignments for the elves
    '''

    pairs = []
    with open('day04-input.txt') as f:
        pairs = f.read().splitlines()
    return pairs

def part_one():
    '''
        Returns the number of elves that have a section assignment that fully contain the other elfs assignment
    '''

    count = 0
    pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
    for pair in get_pairs():
        result = re.search(pattern, pair)
        elf1 = [int(result.group(1)),int(result.group(2))]
        elf2 = [int(result.group(3)),int(result.group(4))]
        if fully_contains(elf1, elf2):
            count += 1

    return count

def part_two():
    '''
        Returns the number of elves that have any overlap in their section assignments with another elf
    '''
    
    count = 0
    pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
    for pair in get_pairs():
        result = re.search(pattern, pair)
        elf1 = [int(result.group(1)),int(result.group(2))]
        elf2 = [int(result.group(3)),int(result.group(4))]
        if overlaps_at_all(elf1, elf2):
            count += 1

    return count

def fully_contains(elf1, elf2):
    '''
        Checks if one of the two assignments is fully contained within the other
    '''

    #return ( elf1[0] >= elf2[0] and elf1[1] <= elf2[1] ) or ( 
    #         elf2[0] >= elf1[0] and elf2[1] <= elf1[1] )
    r1 = range(elf1[0], elf1[1] + 1)
    r2 = range(elf2[0], elf2[1] + 1)
    return (elf2[0] in r1 and elf2[1] in r1) or (elf1[0] in r2 and elf1[1] in r2)

def overlaps_at_all(elf1, elf2):
    '''
        Checks if there is any overlap at all between the two assignments
    '''

    #return ( elf2[1] >= elf1[0] >= elf2[0] ) or ( 
    #         elf2[1] >= elf1[1] >= elf2[0] ) or ( 
    #         elf1[1] >= elf2[0] >= elf1[0] ) or ( 
    #         elf1[1] >= elf2[1] >= elf1[0] )
    r1 = range(elf1[0], elf1[1] + 1)
    r2 = range(elf2[0], elf2[1] + 1)
    return elf2[0] in r1 or elf2[1] in r1 or elf1[0] in r2 or elf1[1] in r2

if __name__ == "__main__":
    print(f"Day 4 part 1: {part_one()}")
    print(f"Day 4 part 2: {part_two()}")