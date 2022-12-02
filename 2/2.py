filename = 'input.txt'

with open(filename) as file:
    plays = []
    for line in file:
        plays.append(line.rstrip('\n').split(' '))

    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    # Your total score is the sum of your scores for each round.
    # The score for a single round is the score for the shape you selected
    # (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the
    # outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

    # round 1
    round_1_score = 0
    for play in plays:
        my_play = play[1]
        opponents_play = play[0]
        if opponents_play == 'A':
            if my_play == 'X':
                # draw, 1 + 3 points for each player
                round_1_score += 4
            if my_play == 'Y':
                # win, 2 + 6 points for me
                round_1_score += 8
            if my_play == 'Z':
                # loss, 3 points for me
                round_1_score += 3
        if opponents_play == 'B':
            if my_play == 'X':
                # loss, 1 points for me
                round_1_score += 1
            if my_play == 'Y':
                # draw, 2 + 3 points for me
                round_1_score += 5
            if my_play == 'Z':
                # win, 3 + 6 points for me
                round_1_score += 9
        if opponents_play == 'C':
            if my_play == 'X':
                # win, 6 + 1 points for me
                round_1_score += 7
            if my_play == 'Y':
                # loss, 2 points for me
                round_1_score += 2
            if my_play == 'Z':
                # draw, 3 + 3 points for me
                round_1_score += 6

    print(round_1_score)

    # round 2
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    round_2_score = 0
    for play in plays:
        strategy = play[1]
        opponents_play = play[0]
        if opponents_play == 'A':
            # opponent plays rock
            if strategy == 'X':
                # i need to lose - my play would be scissors
                round_2_score += 3
            if strategy == 'Y':
                # i need to draw - my play would be rock
                round_2_score += 4
            if strategy == 'Z':
                # i need to win - i play paper
                round_2_score += 8
        if opponents_play == 'B':
            # opponent plays paper
            if strategy == 'X':
                # i need to lose - my play would be Rock
                round_2_score += 1
            if strategy == 'Y':
                # i need to draw - my play would be paper
                round_2_score += 5
            if strategy == 'Z':
                # i need to win - i play scissors
                round_2_score += 9
        if opponents_play == 'C':
            # opponent plays scissors
            if strategy == 'X':
                # i need to lose - my play would be Paper
                round_2_score += 2
            if strategy == 'Y':
                # i need to draw - my play would be scissors
                round_2_score += 6
            if strategy == 'Z':
                # i need to win - i play rock
                round_2_score += 7
    print(round_2_score)
