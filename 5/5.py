filename = 'input.txt'

with open(filename) as file:
    stack_1 = ['R', 'Q', 'G', 'P', 'C', 'F']
    stack_2 = ['P', 'C', 'T', 'W']
    stack_3 = ['C', 'M', 'P', 'H', 'B']
    stack_4 = ['R', 'P', 'M', 'S', 'Q', 'T', 'L']
    stack_5 = ['N', 'G', 'V', 'Z', 'J', 'H', 'P']
    stack_6 = ['J', 'P', 'D']
    stack_7 = ['R', 'T', 'J', 'F', 'Z', 'P', 'G', 'L']
    stack_8 = ['J', 'T', 'P', 'F', 'C', 'H', 'L', 'N']
    stack_9 = ['W', 'C', 'T', 'H', 'Q', 'Z', 'V', 'G']

    stacks = [stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]

    operations = []
    for line in file:
        step = []
        raw_step = line.rstrip('\n').split(' ')
        step.append(int(raw_step[1]))
        step.append(int(raw_step[3]))
        step.append(int(raw_step[5]))
        operations.append(step)

    for step in operations:
        source = stacks[step[1] - 1]
        destination = stacks[step[2] - 1]
        for amount in range(step[0]):
            destination.insert(0, source.pop(0))

    print(
        f'solution part 1: {stacks[0][0]}{stacks[1][0]}{stacks[2][0]}{stacks[3][0]}{stacks[4][0]}{stacks[5][0]}{stacks[6][0]}{stacks[7][0]}{stacks[8][0]}')

    stacks = [['R', 'Q', 'G', 'P', 'C', 'F'], ['P', 'C', 'T', 'W'], ['C', 'M', 'P', 'H', 'B'],
              ['R', 'P', 'M', 'S', 'Q', 'T', 'L'], ['N', 'G', 'V', 'Z', 'J', 'H', 'P'], ['J', 'P', 'D'],
              ['R', 'T', 'J', 'F', 'Z', 'P', 'G', 'L'], ['J', 'T', 'P', 'F', 'C', 'H', 'L', 'N'],
              ['W', 'C', 'T', 'H', 'Q', 'Z', 'V', 'G']]

    for step in operations:
        amount = step[0]
        source = stacks[step[1] - 1]
        destination = stacks[step[2] - 1]
        source_get_boxes = source[0:amount]
        stacks[step[2] - 1] = source_get_boxes + stacks[step[2] - 1]
        del stacks[step[1] - 1][0:amount]
    print(
        f'solution part 2: {stacks[0][0]}{stacks[1][0]}{stacks[2][0]}{stacks[3][0]}{stacks[4][0]}{stacks[5][0]}{stacks[6][0]}{stacks[7][0]}{stacks[8][0]}')
