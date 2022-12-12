import numpy as np

def get_trees():
    '''
        Splits input into pairs of section assignments for the elves
    '''

    trees = []
    with open('day08-input.txt') as f:
        trees = f.read().splitlines()
    return np.array([[int(tree) for tree in list(line)] for line in trees])

def part_one():
    '''
    '''

    trees = get_trees()

    num_trees_visible = len(trees) * 2 + len(trees[0]) * 2

    for line in trees:
        for i, tree in enumerate(line):
            print(tree)

    

    
def part_two():
    '''
    '''

if __name__ == "__main__":
    print(f"Day 8 part 1: {part_one()}")
    print(f"Day 8 part 2: {part_two()}")