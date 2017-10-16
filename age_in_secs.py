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
        # Get current month, day, year
        self.current_month = datetime.date.today().month
        self.current_day = datetime.date.today().day
        self.current_year = datetime.date.today().year
        # Determine number of seconds in a day, average month & average year
        self.numsecs_day = 24 * 60 * 60
        self.numsecs_year = 365 * self.numsecs_day
        # NOTE: Added an extra day while doing a 4yr avg to account for leap yr
        self.avg_numsecs_year = ((self.numsecs_year * 4) + self.numsecs_day) // 4
        self.avg_numsecs_month = self.avg_numsecs_year // 12
        
    def menu_options():
        '''Displays Age-In-Secs Menu Options'''
        calc = AgeInSecs() # Init the class
        loop = True

        while loop == True:
            print("=" * 78)
            print(format(' AGE IN SECONDS ', '=^78'))
            print("=" * 78)
            print('Compute the approximate age in seconds of person based on a \
provided \ndate of birth.\n\nOnly ages for dates of birth from 1900 \
and after can be computed\n')
            print("=" * 78)
            print('\tOperation 1: Calculate Your age in seconds')
            print('\tOperation 2:Compare two peoples ages in seconds')
            print('\tOperation 0: Exit Age-In-Secs Calculator')
            print('-' * 78)
        # User Input
            menu_selection = input('Select a menu option [0-2]: ')

        # Handle user's option
            if menu_selection == '1': # One Person's Age-In-Secs
                calc.cal_age_in_secs()
            elif menu_selection == '2': # Compare Ages-In-Secs
                calc.compare_ages()
            elif menu_selection == '0': # Exit
                print('Exiting Age-In-Secs calculator')
                loop = False
            else:
                print('*' * 78)
                print('{0} is NOT a menu Option.'.format(menu_selection))
                print('Try again..........')       



    def cal_age_in_secs(self):
        '''Calculates approximate age in seconds'''
# TODO: Error Checking
        # Get month, day, year of birth
        print( format(' CALCULATE AGE IN SECS ', '=^78'))
        print('-' * 78)
        print('DOB Details')
        month_birth = int(input('Enter month born [1-12]: '))
        day_birth = int(input('Enter day born [1-31]: '))
        year_birth = int(input('Enter month born [YYYY]: '))
        num_secs_1900_dob = ((year_birth - 1900) * self.avg_numsecs_year) + \
                            ((month_birth - 1) * self.avg_numsecs_month) + \
                            (day_birth * self.numsecs_day)

        num_secs_1900_today = ((self.current_year - 1900) * self.avg_numsecs_year) + \
                            ((self.current_month - 1) * self.avg_numsecs_month) + \
                            (self.current_day * self.numsecs_day)

        age_in_secs = num_secs_1900_today - num_secs_1900_dob

        # Display Results - Person's age in seconds
        print( format(' AGE IN SECS RESULTS ', '=^78'))
        print('\nYou are approx. {0:,} seconds old.'.format(age_in_secs))
        print('-' * 78)
        print('\nYou\'re Age in various units of time')
        print('\t{0:,} seconds old.'.format(age_in_secs))
        print('\t{0:,.2f} Minutes old.'.format(age_in_secs/60))
        print('\t{0:,.2f} hours old.'.format(age_in_secs/3600))
        print('\t{0:,.2f} Days old.'.format(age_in_secs/86400))
        print('\t{0:,.2f} Years  old.'.format(age_in_secs/31536000))
    
    def compare_ages(self):
        '''Compares two peoples ages in secs.'''

        # Get month, day, year of birth
# TODO: Error Checking
        
        print( format(' CALCULATE AGE DIFFERENCE ', '=^78'))
        print('Person1 - DOB Details')
        print('-' * 78)
        month_birth_p1 = int(input('Enter Month Born [1-12]: '))
        day_birth_p1 = int(input('Enter Day of Birth [1-31]: '))
        year_birth_p1 = int(input('Enter Year of Birth [YYYY]: '))

        print('-' * 78)
        print('Person2 - DOB Details')
        month_birth_p2 = int(input('Enter Month Born [1-12]: '))
        day_birth_p2 = int(input('Enter Day of Birth [1-31]: '))
        year_birth_p2 = int(input('Enter Year of Birth [YYYY]: '))


        # Calculate approximate age in second
        numsecs_1900_dob_p1 = ((year_birth_p1 - 1900) * self.avg_numsecs_year) + \
                                ((month_birth_p1 - 1) * self.avg_numsecs_month) + \
                                (day_birth_p1 * self.numsecs_day)

        numsecs_1900_dob_p2 = ((year_birth_p2 - 1900) * self.avg_numsecs_year) + \
                                ((month_birth_p2 - 1) * self.avg_numsecs_month) + \
                                 (day_birth_p2 * self.numsecs_day)

        numsecs_1900_today = ((self.current_year - 1900) * self.avg_numsecs_year) + \
                            ((self.current_month - 1) * self.avg_numsecs_month) + \
                            (self.current_day * self.numsecs_day)

        age_in_secs_p1 = numsecs_1900_today - numsecs_1900_dob_p1
        age_in_secs_p2 = numsecs_1900_today - numsecs_1900_dob_p2
        age_difference = abs(age_in_secs_p1 - age_in_secs_p2)

        # Display Results - Person's age in seconds
        print( format(' AGE DIFFERENCE IN SECS RESULTS ', '=^78'))
        print('\nYou\'re approx. ages are {0:,} seconds apart.'.format(age_difference))
        print('-' * 78)
        print('\nYou\'re Age difference in various units of time')
        print('\t{0:,} seconds'.format(age_difference))
        print('\t{0:,.2f} Minutes'.format(age_difference/60))
        print('\t{0:,.2f} hours'.format(age_difference/3600))
        print('\t{0:,.2f} Days'.format(age_difference/86400))
        print('\t{0:,.2f} Years '.format(age_difference/31536000))

if __name__ == '__main__':
    AgeInSecs.menu_options()