filename = 'input.txt'

with open(filename) as file:
    rucksacks = []
    rucksacks_compartments = []
    for line in file:
        rucksack_items_total = line.rstrip('\n')
        first_compartment = rucksack_items_total[0:len(rucksack_items_total) // 2]
        second_compartment = rucksack_items_total[len(rucksack_items_total) // 2:]
        rucksacks.append(rucksack_items_total)
        rucksacks_compartments.append([first_compartment, second_compartment])

    common_items = []

    for rucksack in rucksacks_compartments:
        already_processed_items = []
        for item in rucksack[0]:
            if rucksack[1].__contains__(item) and not already_processed_items.__contains__(item):
                common_items.append(item)
                already_processed_items.append(item)

    priorities_part_1 = []

    for common_item in common_items:
        priority = 0
        if str(common_item).islower():
            priority = ord(common_item) - 96
        else:
            priority = ord(common_item) - 38
        priorities_part_1.append(priority)

    print(f'Solution Part 1: {sum(priorities_part_1)}')

    groups_of_three = []
    start = 0
    end = len(rucksacks)
    step = 3
    for i in range(start, end, step):
        x = i
        groups_of_three.append(rucksacks[x:x + step])

    badges = []

    for group_of_three in groups_of_three:
        badge_already = []
        for item in group_of_three[0]:
            if group_of_three[1].__contains__(item):
                if group_of_three[2].__contains__(item):
                    if not badge_already.__contains__(item):
                        badges.append(item)
                        badge_already.append(item)
    priorities_part_2 = []
    for badge in badges:
        priority = 0
        if str(badge).islower():
            priority = ord(badge) - 96
        else:
            priority = ord(badge) - 38
        priorities_part_2.append(priority)

    print(f'Solution Part 2: {sum(priorities_part_2)}')
