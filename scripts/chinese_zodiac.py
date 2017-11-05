#!/usr/bin/env python3
'''Chinese Zodiac Program

A simple program that determines the animal and associated characteristics 
from the Chinese Zodiac for a given year of birth. 

This program utilizes the following programming features:
    * tuples
    * datetime module
'''
import datetime



def zodiac_sign():
    '''determine the animal and associated characteristics from the Chinese 
    Zodiac for a given year of birth.'''
    # Init
    zodiac_animals = ('Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 
                        'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig')

    rat = 'forthright, industrious, sensitive, intellectual, sociable'
    ox = 'dependadable, methodical, modest, born leader, patient'
    tiger = 'unpredictable, rebellious, passionate, daring, impulsive'                
    rabbit = 'good friend, kind, soft-spoken, cautious, artistic'
    dragon = 'strong, self-assured, proud, decisive, loyal'
    snake = 'deep-thinker, creative, responsible, calm, purposeful'
    horse = 'cheerful, quick-witted, perceptive, talkative, open-minded'
    goat = 'sincere, sympathetic, shy, generous, mothering'
    monkey = 'motivator, inquisitive, flexible, innovative, problem solver'
    rooster = 'organized, self-assured, decisive, perfectionist, zelous'
    dog = 'honest, unpretentious, idealistic, moralistic, easy going'
    pig = 'peace-loving, hard-working, trusting, understanding, thoughtful'

    characteristics = (rat, ox, tiger, rabbit, dragon, snake, horse, goat, monkey, 
                        rooster, dog, pig)

    terminate = False   # Control program termination

    # Program Greeting
    print(format(' CHINESE ZODIAC PROGRAM ', '=^80'))
    print('Dispaly your zodiac sign and associated personal characteristics.')
    print('~' * 80)

    # Get current year
    current_yr = datetime.date.today().year

    while not terminate:
        # Get year of birth
        try:
            birth_yr = int(input('Enter your year of birth. [YYYY]: '))

            while birth_yr < 1900 or birth_yr > current_yr: # Check that user input is within appropriate range
                print('Invalid year. Please re-enter\n')
                
                try:
                    birth_yr = int(input('Enter your year of birth. [YYYY]: '))

                except ValueError:
                    print('Invalid Input...Enter Numbers only [YYYY]')
            
            # Output results
            cycle_num = (birth_yr - 1900) % 12 
            print('~' * 80)
            print('Your Chinese zodiac sign is the {0}.\n'.format(
                zodiac_animals[cycle_num]))
            print('Your personal characteristics ....\n')
            print(characteristics[cycle_num])
            print('~' * 80)

            # Continue?
            response = input('To try another year enter [y/N]? ')

            while response.upper() != 'Y' and response.upper() != 'N':
                response = input('Please ENTER EITHER "y" OR "n": ')
            
            if response.upper() == 'N':
                terminate = True    # Terminate program
                
        except ValueError:
            print('Invalid Input...Enter Numbers only [YYYY]')

if __name__ == '__main__':
    zodiac_sign()