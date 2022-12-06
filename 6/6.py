filename = 'input.txt'

with open(filename) as file:
    chars = []
    for line in file:
        chars = line.rstrip('\n')
    print(chars)
    counter = 0
    window = []
    for char in chars:
        if len(window) == 4:
            if len(set(window)) == 4:
                print(f'solution part 1: {counter}')
                break
            window.pop(0)
        window.append(char)
        counter += 1
    counter = 0
    window = []
    for char in chars:
        if len(window) == 14:
            if len(set(window)) == 14:
                print(f'solution part 2: {counter}')
                break
            window.pop(0)
        window.append(char)
        counter += 1
