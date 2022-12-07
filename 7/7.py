from treelib import Tree

filename = 'input.txt'


class File:
    def __init__(self, file_name, size):
        self.file_name = file_name
        self.size = size


with open(filename) as file:
    filetree = Tree()
    lines = []
    for line in file:
        lines.append(line.rstrip('\n'))
    current_node = None
    for line in lines:
        if line.startswith('$'):
            command = line.split(' ')[1]
            if command == 'cd':
                dir_name = line.split(' ')[2]
                if dir_name == '..':
                    current_node = filetree.parent(current_node.identifier)
                    continue
                new_node = filetree.create_node(f'{dir_name}', parent=current_node)
                current_node = new_node
            elif command == 'ls':
                continue
                # attach files and dirs to dir
        else:
            if line.split(' ')[0] == 'dir':
                dir_name = line.split(' ')[1]
                if filetree.get_node(f'{dir_name}') is not None:
                    filetree.create_node(f'{dir_name}', parent=current_node)
            else:
                file_size = line.split(' ')[0]
                file_name = line.split(' ')[1]
                filetree.create_node(f'{file_name}', parent=current_node, data=File(file_name, file_size))
    filetree_dict = filetree.to_dict(with_data=True)
    dir_trees = []
    for node in filetree.all_nodes_itr():
        if node.data is None:
            dir_trees.append(filetree.subtree(node.identifier))
    dir_trees_at_most_100000 = []
    size_of_dir_trees_at_most_100000 = 0

    dir_trees_names_sizes = {}
    for tree in dir_trees:
        size = 0
        files = []
        for node_id in tree.expand_tree():
            node = filetree.get_node(node_id)
            if node.data is not None:
                files.append(node)
        for file_node in files:
            size += int(file_node.data.size)
        dir_name = filetree.get_node(tree.root).tag
        dir_trees_names_sizes[dir_name] = size
        if size < 100000:
            dir_trees_at_most_100000.append(tree)
            size_of_dir_trees_at_most_100000 += size
    sorted_dict = sorted(dir_trees_names_sizes.items(), key=lambda item: item[1])
    print(size_of_dir_trees_at_most_100000)
    total_disk_space = 70000000
    free_space = 70000000 - sorted_dict[len(sorted_dict) - 1][1]
    needed_space = 30000000 - free_space
    size_of_dir_to_delete = list(filter(lambda x: x[1] >= needed_space, sorted_dict))[0][1]
    print(size_of_dir_to_delete)
