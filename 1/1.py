filename = 'input.txt'

with open(filename) as file:
    elves = []

    calories = 0
    for line in file:
        if line == '\n':
            elves.append(calories)
            calories = 0
            continue
        else:
            new_cals = int(line.rstrip('\n'))
            calories += new_cals
    print(max(elves))
    elves.sort()
    print(sum(elves[-3:]))
