# Miles Shinsato 11/03/2024 Module 3.2 Assignment

# The purpose of this assignment was to make a flowchart based on the provided below program known as chohan.py
# Additionally, there were several changes to the chohan.py program to be made
# The Input prompt was changed to my initials, "MS: "
# There was a change to be a 12% house fee, up from 10%
# A bonus for if dice total was a 2 or a 7 of 10 mon was added into the program
# Any additional comments that was added to the program below is prefaced with "MS: "

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

# MS: Adding print message to explain the dice_total is equal to 2 or 7, there is a 10 mon bonus
print('Note: If the dice total is a 2 or a 7, you receive a 10 mon bonus!')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('MS: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('MS: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # MS: Adding a function to get the total of dice1 and dice2
    dice_total = dice1 + dice2

    # MS: if statement for when the dice_total is equal to a 2 or a 7
    if dice_total == 2 or dice_total == 7:

        # MS: Print message for if dice_total gets them bonus mon
        print(f'The total of the roll is {dice_total}. You got a 10 mon bonus!')

        # MS: Adding 10 mon to purse
        purse += 10

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.

        # MS: Making adjustment for the House Fee percentage to be 12%
        # MS: Using pot * 12 // 100 instead of pot * 0.12 because it may round the numbers weird
        print('The house collects a', pot * 12 // 100, 'mon fee.')

        # MS: Making a change for the house fee comment in the code
        purse = purse - (pot * 12 // 100)  # The house fee is 12%.
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()