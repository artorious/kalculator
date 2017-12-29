#!/usr/bin/env python3
"""A simple Python3 calculator"""

class ArithmeticOperations():
    """Class holds routines for arithmetic Operations;
    exponentiation, multiplication, division, floor division,
    modulus, addititon and subtraction.
    """
    def __init__(self):
        """Initialization function.
        Sets up attributes and global variables
        """

        # Init
        self.result = 0.0
        self.arg1 = 0.0
        self.arg2 = 0.0

    def get_input(self):
        """(ArithmeticOperations) -> float, float
        Prompt user for two numbers to operate on
        Gets user input and assigns the floats to arg1, arg2
        """
        # init simple error-checking
        valid_value = False

        while not valid_value:
            try:
                self.arg1 = float(input('Enter the first  value: '))
                self.arg2 = float(input('Enter the second  value: ')) 
                valid_value = True # Terminate loop after getting a valid value
            
            except ValueError:
                print('Expected a number')
                print('Please enter a floating-point number')
                continue # Try Again

    def arithmetic_ops_menu(self):
        """Displays Arithmetic  Menu Options."""
        menu_loop = True

        while menu_loop == True:
            print('-' * 80)
            print(format(' Arithmetic Menu Options ', '-^80'))
            print('-' * 80)
            print('\tOperation 1: Addition\t\t(x + y)\n')
            print('\tOperation 2: Subtraction\t(x - y)\n')
            print('\tOperation 3: Exponentiation\t(x ** y)\n')
            print('\tOperation 4: Floor division\t(x // y)\n')
            print('\tOperation 5: Modulus division\t(x % y)\n')
            print('\tOperation 0: Exit Arithmetic Calculator')
            print('-' * 80)
            # User input
            arithmetic_selection = input('Select Operation [0-5]: ')

             # Handle user's option
            if arithmetic_selection == '1': # Addition
                self.addititon_func()

            elif arithmetic_selection == '2': # Subtraction
                self.subtraction_func()

            elif arithmetic_selection == '3': # Exponentiation
                self.exponentiation_func()

            elif arithmetic_selection == '4': # Floor Division
                self.floor_division_func()

            elif arithmetic_selection == '5': # Modulo
                self.modulo_func()

            elif arithmetic_selection == '0':
                print('Exiting Calculator.....')
                menu_loop = False
            else:
                print('*' * 80)
                print('{0}  NOT a menu Option.'.format(arithmetic_selection))
                print('Try again..........')        
    
    def addititon_func(self):
        """Performs addition.  
        Prints a formatted string: arg1 + arg2 = result
        """
        terminate = False # Control task repetition
        while not terminate: 
            print(format(' Addition  ', '.^80' ))
            self.get_input()
            self.result = self.arg1 + self.arg2
            print('Result: \v{0} + {1} = {2:,.2f} or {2:2e}'.format(self.arg1,self.arg2,self.result))
            return_to_menu = input('Press ENTER to calculate again or [q/Q] to Return to Main menu -> ')

            if return_to_menu.upper() == 'Q':
                terminate = True
        

    def subtraction_func(self):
        """Performs subtraction
        Prints a formatted string: arg1 - arg2 = result
        """
        terminate = False # Control task repetition
        while not terminate: 
            print(format(' Subtraction  ', '.^80' ))
            self.get_input()
            self.result = self.arg1 - self.arg2
            print('Result: \v{0} - {1} = {2:,.2f} or {2:2e}'.format(self.arg1,self.arg2,self.result))
            return_to_menu = input('Press ENTER to calculate again or [q/Q] to Return to Main menu -> ')

            if return_to_menu.upper() == 'Q':
                terminate = True
            
    def exponentiation_func(self):
        """exponetiates two numbers from user.
        Prints a formatted string: arg1 ** arg2 = result
        """

        terminate = False # Control task repetition
        while not terminate: 
            print(format(' Exponetiation  ', '.^80' ))
            self.get_input()
            self.result = self.arg1 ** self.arg2
            print('Result: \v{0} ** {1} = {2:,.2f} or {2:2e}'.format(self.arg1,self.arg2,self.result))
            return_to_menu = input('Press ENTER to calculate again or [q/Q] to Return to Main menu -> ')

            if return_to_menu.upper() == 'Q':
                terminate = True

    def floor_division_func(self):
        """performs truncating division on two numbers from user. 
        Prints a formatted string: arg1 // arg2 = result
        """

        terminate = False # Control task repetition
        while not terminate: 
            print(format(' Subtraction  ', '.^80' ))
            self.get_input()
            self.result = self.arg1 // self.arg2
            print('Result: \v{0} // {1} = {2:,.2f} or {2:2e}'.format(self.arg1,self.arg2,self.result))
            return_to_menu = input('Press ENTER to calculate again or [q/Q] to Return to Main menu -> ')

            if return_to_menu.upper() == 'Q':
                terminate = True


    def modulo_func(self):
        """performs modulo division on two numbers from user.  
        Prints a formatted string: arg1 % arg2 = result
        """

        terminate = False # Control task repetition
        while not terminate: 
            print(format(' Subtraction  ', '.^80' ))
            self.get_input()
            self.result = self.arg1 % self.arg2
            print('Result: \v{0} % {1} = {2:,.2f} or {2:2e}'.format(self.arg1,self.arg2,self.result))
            return_to_menu = input('Press ENTER to calculate again or [q/Q] to Return to Main menu -> ')

            if return_to_menu.upper() == 'Q':
                terminate = True


if __name__ == '__main__':
    ArithmeticOperations().arithmetic_ops_menu()