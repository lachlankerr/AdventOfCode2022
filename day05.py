import re

def get_stacks_and_moves():
    '''
        Splits input into crates and moves
    '''

    input = []
    with open('day05-input.txt') as f:
        input = f.read().split('\n\n')

    crates, moves = input[0], input[1]
    crates = crates.splitlines()
    moves = moves.splitlines()

    num_stacks = len(crates[0]) // 4 + 1 # each column has 4 chars including space, but no space at end
    stacks = [[].copy() for x in range(num_stacks)]

    del crates[-1] # remove the row with just numbers
    for line in reversed(crates):
        result = re.findall('.(.)..', line + ' ')
        for i in range(len(result)):
            if result[i] != ' ':
                stacks[i].append(result[i])

    return stacks, moves


def part_one():
    '''
        Moves crates according to CrateMover 9000 rules, 1 crate at a time
        Returns the top crate of each stack
    '''

    stacks, moves = get_stacks_and_moves()

    for move in moves:
        result = list(map(int, re.findall('\d+', move)))
        n = result[0]
        from_stack = result[1] - 1
        to_stack = result[2] - 1
        for i in range(n):
            stacks[to_stack].append(stacks[from_stack].pop())

    top_stacks = ''.join([stack.pop() for stack in stacks])

    return top_stacks


def part_two():
    '''
        Moves crates according to CrateMover 9001 rules, multiple crates at once
        Returns the top crate of each stack
    '''

    stacks, moves = get_stacks_and_moves()

    for move in moves:
        result = list(map(int, re.findall('\d+', move)))
        n = result[0]
        from_stack = result[1] - 1
        to_stack = result[2] - 1
        crane_stack = []
        for i in range(n):
            crane_stack.append(stacks[from_stack].pop())
        stacks[to_stack].extend(reversed(crane_stack))

    top_stacks = ''.join([stack.pop() for stack in stacks])

    return top_stacks

if __name__ == "__main__":
    print(f"Day 5 part 1: {part_one()}")
    print(f"Day 5 part 2: {part_two()}")