# crapts.py

import random

# First, create a sequence with 13 empty sets
def create_sets():
    # creates an empty dict
    dice = {}

    # creates 12 sets which represent dice rolls. Each set is assigned to a key
    for i in range (1,13):
        dice[i] = set()

    return dice

# Second, write two, nested, for-loops to iterate through all 36 combinations of dice, creating 2-tuples. 
def populate_sets(dice):
    for i in range(1,7):
        for j in range(1,7):
            # adds the value of the iterations as a set, to the key in the dictionary
            dice[i+j].add((i, j))
    
    return dice

# third, create the actual program
def main():
    dice = populate_sets(create_sets())

    craps_point = 0

    # lose set
    lose = (dice[2], dice[3], dice[12])

    # win set
    win = (dice[7], dice[11])

    # point set
    point = (dice[4], dice[5], dice[6], dice[8], dice[9], dice[10])

    # emulating rolling two dices with random module
    rolled_dices = (random.randint(1,6), random.randint(1,6))

    print('You\'ve rolled a',rolled_dices[0]+rolled_dices[1], rolled_dices)

    # using for loops to check if the rolled dices are in the sets
    for i in lose:
        if rolled_dices in i:
            print('You\'ve lost!')

    for i in win:
        if rolled_dices in i:
            print('You\'ve won!')

    for i in point:
        if rolled_dices in i:
            print('You\'ve established a craps point! If you roll a', rolled_dices[0]+rolled_dices[1], 'you win')
            # sets the craps point to the set of the index of the two rolled dices
            craps_point = dice[rolled_dices[0]+rolled_dices[1]]
    
    # while loop to keep the game running until you've hit 7 or the craps point
    if craps_point is not 0:
        while(rolled_dices not in dice[7] or rolled_dices in craps_point):
            rolled_dices = (random.randint(1,6), random.randint(1,6))
            print('You\'ve rolled a', rolled_dices[0]+rolled_dices[1], rolled_dices)

            if rolled_dices in dice[7]:
                print('You\'ve lost')
            elif rolled_dices is craps_point:
                print('You\'ve won!')
            else:
                print("Roll again")

    


    
    
main()
