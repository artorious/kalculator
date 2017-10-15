#!/usr/bin/env python3

'''A simple calculator for the travelling salesman problem.'''
__author__ = 'Arthur Ngondo'
__version__ = '$Version: 1.0.0 $'

from math import factorial

def routes_possible():
    '''prompts user for a the number of cities for the traveling salesman 
    problem, and displays the total number of possible routes that can be 
    taken.'''

    print(format(' TRAVELLING SALESMAN ', '=^78'))
    print('Find all the possible routes of travel for a salesman needing to \
visit a given \nset of cities.')
    
    # Prompt for user input
    cities = int(input('How many Cities [0 - 999]: '))
    print('For {0} cities, there are {1:,} possible routes'.format(
        cities, factorial(cities) ))

if __name__ == '__main__':
    routes_possible()