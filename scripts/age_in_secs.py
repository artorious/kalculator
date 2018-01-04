#!/usr/bin/env python3
'''Age in Seconds. 

A Simple script that approximates a person's age in seconds.
The program works for dates of birth from January 1, 1900 to the present.
'''
import datetime
# TODO: Compare ages
class AgeInSecs:
    """
    Class holds routines that approximate age in seconds 
    and compares two people's ages.
    """
    def __init__(self):
        """ Initialize attributes """
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
    
        self.name, self.day_birth, self.month_birth, self.year_birth = (None, None, None, None)

    def calc_age_in_secs(self):
        """(AgeInSecs) -> float

        Returns age in seconds
        """
        num_secs_1900_dob = (
            (int(self.year_birth) - 1900) * self.avg_numsecs_year) + \
            ((int(self.month_birth) - 1) * self.avg_numsecs_month) + \
            (int(self.day_birth) * self.numsecs_day)
        
        num_secs_1900_today = ((self.current_year - 1900) * 
            self.avg_numsecs_year) + ((self.current_month - 1) * 
            self.avg_numsecs_month) + (self.current_day * self.numsecs_day)

        return num_secs_1900_today - num_secs_1900_dob
    
    def display_age(self, age_in_secs=0):
        """
         Display Person's age in various units of time
        """
        print(format(' AGE IN SECS RESULTS  - {0} ', '=^80').format(self.name))
        print()
        print('{0}\'s Age in various units of time'.format(self.name))
        print('~' * 80)
        print('\n\t{0:,} seconds old.'.format(age_in_secs))
        print('\t{0:,.2f} Minutes old.'.format(age_in_secs/60))
        print('\t{0:,.2f} hours old.'.format(age_in_secs/3600))
        print('\t{0:,.2f} Days old.'.format(age_in_secs/86400))
        print('\t{0:,.2f} Years  old.'.format(age_in_secs/31536000))

    def display_age_comparisons(self, age_in_secs_p1, age_in_secs_p2):
        """
         Display comparison of ages in various units of time
        """
        pass
    
    def get_age_details(self):
        """(AgeInSecs)
        Prompt user for DD-MM-YY
        """
        self.name = input('Enter your Name: ')
        # Get month, day, year of birth
        print('Day of Birth :', end='')
        self.day_birth = self.get_int_in_range(1, 31)
        print('Month of Birth :', end='')
        self.month_birth = self.get_int_in_range(1, 12)
        print('Year of Birth :', end='')
        self.year_birth = self.get_int_in_range(1900, self.current_year)
        
        
    def get_int_in_range(self, first, last):
        """(int, int) -> int
        Prompt user for an integer within the specified range
        <first> is either a min or max acceptable value.
        <last> is the corresponding other end of the range, either a min or max 
        acceptable value.
        Returns an acceptable value from the user
        """
        if isinstance(first, int) and isinstance(last, int):
            if first > last:    # If larger no. is provided 1st
                first, last = last, first   # Switch the parameters
            # Insist on value in the range <first>...<last>
            try:
                in_value = int(input('Enter value in the range {0} .... {1} : '\
                        .format(first, last)))
            
                while in_value < first or in_value > last:
                    print('{0} IS NOT in the range {1} .... {2}'.format(in_value, first, last))
                    in_value = int(input('Try again: '))
                
                return in_value

            except ValueError as err:
                return err
        else:
            return 'Expected an integers. int_in_range({0}, {1}) not surpported' \
                    .format(type(first), type(last))


def menu_options():
    """ Displays Age-In-Secs Menu Options """
    calc = AgeInSecs() # Init the class
    menu_loop = True
    while menu_loop == True: # Enter menu loop
        print("=" * 80)
        print(format(' AGE IN SECONDS ', '=^80'))
        print("=" * 80)
        print(format(' Compute the approximate age in seconds of person', '-^80')) 
        print(format(' based on a provided date of birth. ', '-^80')) 
        print(format(' Only ages for dates from 1900 and after can be computed. ', '-^80'))
        print("=" * 80)
        print('\tOperation 1: Calculate Your age in seconds')
        print('\tOperation 2: Compare two peoples ages in seconds')
        print('\tOperation 0: Exit Age-In-Secs Calculator')
        print('-' * 80)
    # User Input
        menu_selection = input('Select a menu option [0-2]: ')

    # Handle user's option
        if menu_selection == '1': # One Person's Age-In-Secs
            calculation_loop = False
            while not calculation_loop: # Enter calculation loop
                print()
                calc.get_age_details()
                calc.display_age(calc.calc_age_in_secs())
                print()
                response = input('Q)uit to go back OR E)nter to repeat >>> ')
                if response.strip().upper() == 'Q':
                    calculation_loop = True
                else:
                    continue
            
        elif menu_selection == '2': # Compare Ages-In-Secs
            calculation_loop = False
            while not calculation_loop: # Enter calculation loop
                print( )
                calc.get_age_details()
                calc.display_age(calc.calc_age_in_secs())
                print()
                response = input('Q)uit to go back OR E)nter to repeat')
                if response.strip().upper() == 'Q':
                    calculation_loop = True
                else:
                    continue
        elif menu_selection == '0': # Exit
            print('Exiting Age-In-Secs calculator')
            menu_loop = False # Exit menu loop       
        else:
            print('*' * 80)
            print('{0} is NOT a menu Option.'.format(menu_selection))
            print('Try again..........')       

if __name__ == '__main__':
    menu_options()


