from anytree import Node
filename = 'input.txt'

with open(filename) as file:
    lines = []
    for line in file:
        lines.append(line.rstrip('\n'))
    root = Node('/')
    current_node = root
    for line in lines:
        if line.startswith('$'):
            command = line.split(' ')[1]
            if command == 'cd':
                dir_name = line.split(' ')[2]
                newNode = Node(f'{dir_name}', parent=current_node)
            elif line.split(' ')[2] == 'ls':
                # attach files and dirs to dir

    print('debug')
