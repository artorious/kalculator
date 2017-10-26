#!/usr/bin/env python3
'''Coin Change Exercise Program

The script implements an exercise for children learning to count change($). 
It displays a random value between 1 to 99 (cents), and asks the user to enter
a set of values(coins) that add up to the amount shown.
'''

import random

def coin_change_calculator():
    '''Coin Change Exercise Routine'''
    # Program Greeting
    print('=' * 80)
    print(format(' Coin Change Exercise Program ', '=^80'))
    print('=' * 80)
    print('The purpose of this exercise is to enter a number of coin values')
    print('that add up to a diaplayed target value.\n')
    print('Enter coins values as 1-penny, 5-nickel, 10-dime and 25-quarter')
    print('-' * 80)
    print('Hit RETURN [Enter] after the last entered coin value.')
    print('=' * 80)


    # Init
    terminate = False # For termination control of main loop (program)
    empty_str = '' # For indicating when user ends coin entries

    # Start Game
    while not terminate:
        # Init
        amount = random.randint(1, 99) # Randomly generate a coin value for the user to match
        print('Enter coins that add-up-to {0} cents, one-per-line\n'.format(amount))
        game_over = False # For termination control of current game
        total = 0

        while not game_over:
            valid_entry = False # Control whether user is prompted for another game

            while not valid_entry: 
                if total == 0:
                    entry = input('Enter First Coin: ')
                else:
                    entry = input('Enter next coin: ')
                # Check for entry's membership
                if entry in (empty_str, '1', '5', '10', '25'):
                    valid_entry = True
                else: # Continue coin entry loop
                    print('INVALID ENTRY!... Continue...')

            if entry == empty_str:
                if total == amount: # Correct answer
                    print(format(' CORRECT! ', '*^80'))
                else: # Wrong  Answer (falls-short)
                    print('-' * 80)
                    print('SORRY - You only entered {0} cents.'.format(total))
                    print('=' * 80)
            
                game_over = True # End current Game
            else:
                total += int(entry)
                
                if total > amount:# Wrong  Answer (exceeds)
                    print('-' * 80)
                    print('SORRY - Total amont exceeds {0} cents'.format(amount)) 
                    print('=' * 80)
                    game_over = True # End Current Game
            # Prompt user for another game
            if game_over: 
                entry = input('\nTry Again [y/N]?: ')

                if entry.upper() == 'N':
                    terminate = True # Terminate program

 
    print('Thanks for playing..... Goodbye')

if __name__ == '__main__':
    coin_change_calculator()



