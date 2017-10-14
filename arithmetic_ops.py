#!/usr/bin/env python3
'''A simple Python3 calculator'''

class ArithmeticOperations(object):
    '''Class holds routines for arithmetic Operations;
    exponentiation, multiplication, division, floor division,
    modulus, addititon and subtraction.
    '''

    def __init__(self):
        '''Initialization function.'''
        pass
    
    def arithmetic_ops_menu():
        '''Displays Arithmetic  Menu Options'''
        calc = ArithmeticOperations() # Init the class
        loop = True

        while loop == True:
            print('-' * 78)
            print(format(' Arithmetic Menu Options ', '-^78'))
            print('-' * 78)
            print('\tOperation 1: Addition\t\t(x + y)\n')
            print('\tOperation 2: Subtraction\t(x - y)\n')

            print('\tOperation 3: Exponentiation\t(x ** y)\n')
            print('\tOperation 4: Floor division\t(x // y)\n')
            print('\tOperation 5: Modulus division\t(x % y)\n')
            print('\tOperation 0: Exit Arithmetic Calculator')
            print('-' * 78)
            # User input
            arithmetic_selection = input('Select Operation [0-8]: ')

            # Handle user's option
            if arithmetic_selection == '1': # Addition
                pass

            elif arithmetic_selection == '2': # Subtraction
                pass

            elif arithmetic_selection == '3': # Exponentiation
                pass

            elif arithmetic_selection == '4': # Floor Division
                pass

            elif arithmetic_selection == '5': # Modulo
                pass

            elif arithmetic_selection == '0':
                print('Exiting Calculator.....')
                loop = False
            else:
                print('Unrecognized Command. Try Again...')


    def addititon_func(self):
        '''adds up two numbers from user.
        Takes integers, floating-point and scientific notation numbers. 
        
        Prints num1 + num2 = sum (exactly two decimal places.)
        ''' 
        pass
    def subtraction_func(self):
        '''subtracts two numbers from user. 
        Takes integers, floating-point and scientific notation numbers. 
        
        Prints num1 - num2 = difference (exactly two decimal places.)
        '''
        pass
    def exponentiation_func(self):
        '''exponetiates two numbers from user.
        Takes integers, floating-point and scientific notation numbers. 
        
        Prints num1 - num2 = exponent (exactly two decimal places.)
        ''' 
        pass
    def floor_division_func(self):
        '''performs truncating division on two numbers from user. 
        Takes integers, floating-point and scientific notation numbers. 
        
        Prints num1 // num2 = result (exactly two decimal places.)
        '''
        pass
    def modulo_func(self):
        '''performs modulo division on two numbers from user.  
        Takes integers, floating-point and scientific notation numbers. 
        
        Prints num1 % num2 = result (exactly two decimal places.)
        '''
        pass

if __name__ == '__main__':
    ArithmeticOperations.arithmetic_ops_menu()