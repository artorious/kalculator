#!/usr/bin/env python3
''' A simple menu-driven calculator

Features include:
    Arithmetic Operations on two values
    SETI - Search for Extra-terrestrial Intelligence
    Travelling Salesman Problem
    Age in Seconds
'''

from travelling_salesman import routes_possible
from arithmetic_ops import ArithmeticOperations as kalq
from seti_drake_eq import drake_eq

class CalculateSomething(object):
    '''Class holds the routines for various inputs.'''
    
    def __init__(self):
        '''Intialization function'''
        pass

    def calculator_menu():
        '''loop displays a list of options that the user can perform'''

        loop = True

        while loop==True:
            print('=' * 78)
            print(format(' CALCULATOR MENU ', '=^78'))
            print('=' * 78)
            # Prompt the user for type of calculation
            print('\n\t Option 1 - Simple Arithmetic operations.\n\n\t\t\t(**) \
Exponentiation, (*) Multiplication, (/) Division,\n\t\t\t(//) Floor \
Division,(%) Modulus, (+) Addition,\n\t\t\t(-) Subtraction')

            print('\n\t Option 2 - Search for Extra-terrestrial Intelligence ')
            print('\t\t\tCalculate the Drake Equation')
            print('\n\t Option 3 - 1st Day of the month')
            print('\n\t Option 4 - Age in Seconds ')
            print('\n\t Option 5 - Travelling Salesman ')
            print('\t\t\tFind all possible routes of travel for salesman \
needing \n\t\t\tto visit a given set of cities')
            print('\n\t Option 0 - Exit')
            print('=' * 78)

            # Wait for user input
            menu_selection = input('Enter Option Number [0 - 5]: ')

            if menu_selection == '1': # Arithmetic Operations
                kalq.arithmetic_ops_menu()
                
            elif menu_selection == '2': # SETI
                print('*' * 78)
                drake_eq()
                print('*' * 78)
            
            elif menu_selection == '3': # 1st Day of the month
                pass

            elif menu_selection == '4': # Age in secs
                pass

            elif menu_selection == '5': # Travelling Salesman
                print('*' * 78)
                routes_possible()
                print('*' * 78)

            elif menu_selection == '0': # Exit
                print('Exiting......Goodbye!')
                loop = False

            else:
                print('*' * 78)
                print('{0} is NOT a menu Option.'.format(menu_selection))
                print('Try again..........')


if __name__ == '__main__':
    CalculateSomething.calculator_menu()