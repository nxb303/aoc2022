filename = 'input.txt'

with open(filename) as file:
    lines = []
    for line in file:
        lines.append(line.rstrip('\n').split(','))

    assignments = []
    double_assignments = 0
    overlap_at_all = 0
    for line in lines:
        assignments.append([line[0].split('-'), line[1].split('-')])
    for assignment in assignments:
        first_assignment_indexes = []
        second_assignment_indexes = []
        for i in range(int(assignment[0][0]), int(assignment[0][1]) + 1):
            first_assignment_indexes.append(i)
        for i in range(int(assignment[1][0]), int(assignment[1][1]) + 1):
            second_assignment_indexes.append(i)

        if all([item in first_assignment_indexes for item in second_assignment_indexes]) or all(
                [item in second_assignment_indexes for item in first_assignment_indexes]):
            double_assignments += 1
        for item in first_assignment_indexes:
            if second_assignment_indexes.__contains__(item):
                overlap_at_all += 1
                break
    print(double_assignments)
    print(overlap_at_all)
