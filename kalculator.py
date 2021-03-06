#!/usr/bin/env python3
''' A simple menu-driven calculator

Features include:
    Arithmetic Operations on two values
    SETI - Search for Extra-terrestrial Intelligence
    Travelling Salesman Problem
    Age in Seconds
'''

from scripts.travelling_salesman import routes_possible
from scripts.arithmetic_ops import ArithmeticOperations as kalq
from scripts.seti_drake_eq import drake_eq
from scripts.age_in_secs import menu_options
from scripts.coin_change import coin_change_calculator
from scripts.chinese_zodiac import zodiac_sign
from scripts.password_encrypt_decrypt import encrypt_decrypt
from scripts.calendar_year import calendar
from scripts.temp_converter import convert_temp

class CalculateSomething(object):
    '''Class holds the routines for various inputs.'''
    
    def __init__(self):
        '''Intialization function'''
        pass

    def calculator_menu():
        '''menu_loop displays a list of options that the user can perform'''
        # Init
        menu_loop = True

        while menu_loop==True:
            print('=' * 80)
            print(format(' CALCULATOR MENU ', '=^80'))
            print('=' * 80)
            # Prompt the user for type of calculation
            print('\n\t Option 1 - Simple Arithmetic operations.\n\n\t\t\t(**) \
Exponentiation, (*) Multiplication, (/) Division,\n\t\t\t(//) Floor \
Division,(%) Modulus, (+) Addition,\n\t\t\t(-) Subtraction')

            print('\n\t Option 2 - Search for Extra-terrestrial Intelligence ')
            print('\t\t\tCalculate the Drake Equation')
            print('\n\t Option 3 - Calender - Month View')
            print('\n\t Option 4 - Age in Seconds ')
            print('\t\t\tCalculate age in seconds and compare two people\'s ages.')
            print('\n\t Option 5 - Travelling Salesman ')
            print('\t\t\tFind all possible routes of travel for salesman \
needing \n\t\t\tto visit a given set of cities')
            print('\n\t Option 6 - Coin Change Program ')
            print('\t\t\tAn exercise for children learning to count change')
            print('\n\t Option 7 - Chinese Zodiac Program ')
            print('\t\t\tDetermine the animal and associated characteristics from \
            \n\t\t\tthe Chinese Zodiac for a given year of birth.')
            print('\n\t Option 8 - Password Encryption/Decryption Program ')
            print('\t\t\tEncrypt/Decrypt a Pass-Phrase.')
            print('\n\t Option 9 - Calender - Year View')
            print('\n\t Option 10 - Temperature Conversion Program')
            print('\n\t Option 0 - Exit')
            print('=' * 80)

            # Wait for user input
            menu_selection = input('Enter Option Number [0 - 9]: ')

            if menu_selection == '1': # Arithmetic Operations
                kalq().arithmetic_ops_menu()
                
            elif menu_selection == '2': # SETI
                print('*' * 80)
                drake_eq()
                print('*' * 80)
            
            elif menu_selection == '3': # Calendar month-view
                pass
            elif menu_selection == '4': # Age in secs
                print('*' * 80)
                menu_options()
                print('*' * 80)

            elif menu_selection == '5': # Travelling Salesman
                print('*' * 80)
                routes_possible()
                print('*' * 80)

            elif menu_selection == '6': # Coin Change
                print('*' * 80)
                coin_change_calculator()
                print('*' * 80)
            
            elif menu_selection == '7': # Chinese Zodiac
                print('*' * 80)
                zodiac_sign()
                print('*' * 80)
            
            elif menu_selection == '8': # Encrypt/Decrypt
                print('*' * 80)
                encrypt_decrypt()
                print('*' * 80)

            elif menu_selection == '9': # Calendar Year
                print('*' * 80)
                calendar()
                print('*' * 80)

            elif menu_selection == '10': # Temperature Conversion
                print('*' * 80)
                convert_temp()
                print('*' * 80)

            elif menu_selection == '0': # Exit
                print('Exiting......Goodbye!')
                menu_loop = False

            else:
                print('*' * 80)
                print('{0} is NOT a menu Option.'.format(menu_selection))
                print('Try again..........')


if __name__ == '__main__':
    CalculateSomething.calculator_menu()
