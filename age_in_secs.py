#!/usr/bin/env python3
'''Age in Seconds. 

A Simple script that approximates a person's age in seconds.
The program works for dates of birth from January 1, 1900 to the present.
'''

import datetime

class AgeInSecs(object):
    '''Class holds routines that approximate age in seconds 
    and compares two people's ages. '''
    
    def __init__(self):
        '''Initialization function.'''
        # Compute current month, day, year
        self.current_month = datetime.date.today().month
        self.current_day = datetime.date.today().day
        self.current_year = datetime.date.today().year
        # Hard-code no. of secs in a day, avg. month & avg. year
        self.numsecs_day = 24 * 60 * 60
        self.numsecs_year = 365 * self.numsecs_day
        # NOTE: Added an extra day while doing a 4yr avg to account for leap yr
        self.avg_numsecs_year = ((self.numsecs_year * 4) + self.numsecs_day) \
                                // 4
        self.avg_numsecs_month = self.avg_numsecs_year // 12
        
    def menu_options():
        '''Displays Age-In-Secs Menu Options'''
        
        calc = AgeInSecs() # Init the class
        
        menu_loop = True

        while menu_loop == True: # Enter menu loop

            print("=" * 80)
            print(format(' AGE IN SECONDS ', '=^80'))
            print("=" * 80)
            print(format(' Compute the approximate age in seconds of person', 
'-^80')) 
            print(format(' based on a provided date of birth. ', '-^80')) 
            print(format(' Only ages for dates from 1900 and after can be \
computed. ', '-^80'))
            print("=" * 80)
            print('\tOperation 1: Calculate Your age in seconds')
            print('\tOperation 2: Compare two peoples ages in seconds')
            print('\tOperation 0: Exit Age-In-Secs Calculator')
            print('-' * 80)
        # User Input
            menu_selection = input('Select a menu option [0-2]: ')

        # Handle user's option
            if menu_selection == '1': # One Person's Age-In-Secs
                calc.cal_age_in_secs()
            
            elif menu_selection == '2': # Compare Ages-In-Secs
                calc.compare_ages()
            
            elif menu_selection == '0': # Exit
                print('Exiting Age-In-Secs calculator')
            
                menu_loop = False # Exit menu loop
            
            else:
                print('*' * 80)
                print('{0} is NOT a menu Option.'.format(menu_selection))
                print('Try again..........')       



    def cal_age_in_secs(self):
        '''Calculates approximate age in seconds'''

        calculation_loop = True

        while calculation_loop == True: # Enter calculation loop
        
            print( format(' CALCULATE AGE IN SECS ', '=^80'))
            print('-' * 80)
            print('DOB Details - MM-DD-YYYY')

# TODO: Improve Error-checking            
            # Get month, day, year of birth
            month_birth = input('Enter month born [1-12]: ')
            # Error checking: Check for valid month of birth input
            
            try:
            
                if int(month_birth) in range(1, 13):
                    day_birth = input('Enter day born [1-31]: ')
                
                    
                    # Error checking: Check for valid day of birth input
                    try:
            
                        if int(day_birth) in range(1, 32):
                            year_birth = input('Enter year born [YYYY]: ')

                            # Error checking: Check for valid year of birth input
                            try:
            
                                if int(year_birth) in range(1900, self.current_year):                        
                                    num_secs_1900_dob = \
                                        ((int(year_birth) - 1900) * 
                                        self.avg_numsecs_year) + \
                                        ((int(month_birth) - 1) * 
                                        self.avg_numsecs_month) + \
                                        (int(day_birth) * self.numsecs_day)

                                    num_secs_1900_today = \
                                        ((self.current_year - 1900) * 
                                        self.avg_numsecs_year) + \
                                        ((self.current_month - 1) * 
                                        self.avg_numsecs_month) + \
                                        (self.current_day * self.numsecs_day)

                                    age_in_secs = \
                                        num_secs_1900_today - num_secs_1900_dob

                                    # Display Results - Person's age in seconds
                                    print(format(' AGE IN SECS RESULTS ', 
                                        '=^80'))
                                    print('\nApprox. Age: {0:,} seconds old.'
                                        .format(age_in_secs))
                                    print('~' * 80)
                                    print('\nYou\'re Age in various units of time')
                                    print('~' * 80)
                                    print('\n\t{0:,} seconds old.'
                                        .format(age_in_secs))
                                    print('\t{0:,.2f} Minutes old.'
                                        .format(age_in_secs/60))
                                    print('\t{0:,.2f} hours old.'
                                        .format(age_in_secs/3600))
                                    print('\t{0:,.2f} Days old.'
                                        .format(age_in_secs/86400))
                                    print('\t{0:,.2f} Years  old.'
                                        .format(age_in_secs/31536000))                        

                                    calculation_loop = False

                            except ValueError as invalid_year_input:
                                print('-' * 80)
                                print('ERROR: ', invalid_year_input)
                                print('*' * 80)
                                print('\n{0} is not an integer in range [1900 \
- {1}]....TRY AGAIN...\n'.format(year_birth, self.current_year))
            
                    except ValueError as invalid_day_input:
                        print('-' * 80)
                        print('ERROR: ', invalid_day_input)
                        print('*' * 80)
                        print('\n{0} is not an integer in range [1-31]....TRY \
AGAIN...\n'.format(day_birth))  

            except ValueError as invalid_month_input:
                print('-' * 80)
                print('ERROR: ', invalid_month_input)
                print('*' * 80)
                print('\n{0} is NOT an integer in range [1-12]....TRY AGAIN....\
\n'.format(month_birth))

            else:
                print('\n....TRY AGAIN...\n')
                calculation_loop = False
                 
           
        
        
    
    def compare_ages(self):
        '''Compares two peoples ages in secs.'''

        calculation_loop = True

        while calculation_loop == True:
            
            print( format(' CALCULATE AGE DIFFERENCE ', '=^80'))
            print('Person1 - DOB Details')
            print('-' * 80)

            # Get month, day, year of birth
            month_birth_p1 = input('Enter Month Born [1-12]: ')
  # TODO: Improve Error-checking          
            try:
# Error checking: Check for valid month of birth input
                if int(month_birth_p1) in range(1,13):
                    day_birth_p1 = input('Enter Day of Birth [1-31]: ')

                    try:
                # Error checking: Check for valid day of birth input
                        if int(day_birth_p1) in range(1,32):
                            year_birth_p1 = input('Enter Year of Birth [YYYY]: ')
                            
                            try:   
# Error checking: Check for valid year of birth input
                                if int(year_birth_p1) in range(1900, 
                                    self.current_year + 1):
                                    print('-' * 80)
                                    print('Person2 - DOB Details')
                                    print('-' * 80)
                                    month_birth_p2 = input(
                                        'Enter Month Born [1-12]: ')

                                    try:
# Error checking: Check for valid month of birth input
                                        if int(month_birth_p2) in range(1,13):
                                            day_birth_p2 = input(
                                                'Enter Day of Birth [1-31]: ')

                                            try:
# Error checking: Check for valid day of birth input
                                                if int(day_birth_p2) in range(1, 32):
                                                    year_birth_p2 = input(
                                                        'Enter Year of Birth [YYYY]: ')
                                                   # Error checking: Check for valid year of birth input 
                                                    try:
                                                        
                                                        if int(year_birth_p2) in range(1900, self.current_year + 1):
                                                            # Calculate approximate age in second
                                                            numsecs_1900_dob_p1 = ((int(year_birth_p1) - 1900) * self.avg_numsecs_year) \
                                                                + ((int(month_birth_p1) - 1) * self.avg_numsecs_month) + \
                                                                (int(day_birth_p1) * self.numsecs_day)

                                                            numsecs_1900_dob_p2 = ((int(year_birth_p2) - 1900) * self.avg_numsecs_year) + \
                                                                ((int(month_birth_p2) - 1) * self.avg_numsecs_month) + \
                                                                (int(day_birth_p2) * self.numsecs_day)

                                                            numsecs_1900_today = ((self.current_year - 1900) * self.avg_numsecs_year) + \
                                                                ((self.current_month - 1) * self.avg_numsecs_month) + \
                                                                (self.current_day * self.numsecs_day)

                                                            age_in_secs_p1 = numsecs_1900_today - numsecs_1900_dob_p1
                                                            age_in_secs_p2 = numsecs_1900_today - numsecs_1900_dob_p2
                                                            age_difference = abs(age_in_secs_p1 - age_in_secs_p2)

                                                            # Display Results - Person's age in seconds
                                                            print( format(' AGE DIFFERENCE IN SECS RESULTS ', '=^80'))
                                                            print('\nYou\'re approx. ages are {0:,} seconds apart.'.format(age_difference))
                                                            print('-' * 80)
                                                            print('\nYou\'re Age difference in various units of time')
                                                            print('\n\t{0:,} seconds'.format(age_difference))
                                                            print('\t{0:,.2f} Minutes'.format(age_difference/60))
                                                            print('\t{0:,.2f} hours'.format(age_difference/3600))
                                                            print('\t{0:,.2f} Days'.format(age_difference/86400))
                                                            print('\t{0:,.2f} Years '.format(age_difference/31536000))

                                                            calculation_loop = False
                                                    
                                                    except ValueError as invalid_year_input_p2:
                                                        print('-' * 80)
                                                        print('ERROR: ', invalid_year_input_p2)
                                                        print('*' * 80)
                                                        print('\n{0} is not an integer in range [1-31]....TRY AGAIN...\n'.format(year_birth_p2))

                                            except ValueError as invalid_day_input_p2:
                                                print('-' * 80)
                                                print('ERROR: ', invalid_day_input_p2)
                                                print('*' * 80)
                                                print('\n{0} is not an integer in range [1-31]....TRY AGAIN...\n'.format(day_birth_p2))

                                    except ValueError as invalid_month_input_p2:
                                        print('-' * 80)
                                        print('ERROR: ', invalid_month_input_p2)
                                        print('*' * 80)
                                        print('\n{0} is not an integer in range [1-31]....TRY AGAIN...\n'.format(month_birth_p2))

                            except ValueError as invalid_year_input_p1:
                                print('-' * 80)
                                print('ERROR: ', invalid_year_input_p1)
                                print('*' * 80)
                                print('\n{0} is not an integer in range [1-31]....TRY AGAIN...\n'.format(year_birth_p1))

                    except ValueError as invalid_day_input_p1:
                        print('-' * 80)
                        print('ERROR: ', invalid_day_input)
                        print('*' * 80)
                        print('\n{0} is not an integer in range [1-31]....TRY AGAIN...\n'.format(day_birth_p1))
                        

            except ValueError as invalid_month_input:
                print('-' * 80)
                print('ERROR: ', invalid_month_input)
                print('*' * 80)
                print('\n{0} is NOT an integer in range [1-12]....TRY AGAIN....\
\n'.format(month_birth_p1))
            else:
                print('\n....TRY AGAIN...\n')
                calculation_loop = False

        

if __name__ == '__main__':
    AgeInSecs.menu_options()