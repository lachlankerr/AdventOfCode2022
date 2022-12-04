import re

def get_pairs():
    '''
        Splits input into each section assignment pairs
    '''

    pairs = []
    with open('day04-input.txt') as f:
        pairs = f.read().splitlines()
    return pairs

def part_one():
    '''
    
    '''

    count = 0
    pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
    for pair in get_pairs():
        result = re.search(pattern, pair)
        first = [int(result.group(1)),int(result.group(2))]
        second = [int(result.group(3)),int(result.group(4))]
        if is_pair_contained(first, second):
            count += 1

    return count

def part_two():
    '''
    
    '''
    
    count = 0
    pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
    for pair in get_pairs():
        result = re.search(pattern, pair)
        first = [int(result.group(1)),int(result.group(2))]
        second = [int(result.group(3)),int(result.group(4))]
        if overlaps_at_all(first, second):
            count += 1

    return count

def is_pair_contained(first, second):
    return ( first[0] >= second[0] and first[1] <= second[1] ) or ( second[0] >= first[0] and second[1] <= first[1] )

def overlaps_at_all(first, second):
    return first[1] >= second[0] or second[1] >= first[0]

if __name__ == "__main__":
    print(f"Day 4 part 1: {part_one()}")
    print(f"Day 4 part 2: {part_two()}")