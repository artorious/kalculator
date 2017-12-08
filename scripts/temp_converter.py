#!/usr/bin/env python3
'''Temperature Conversion Program
The program allows a user to convert a range of values from Fahrenheit to Celsius, 
or Celsius to Fahrenheit.
The script utilizes the following programming features.
    ➤ value-returning functions
    ➤ non-value-returning functions
'''
def display_welcome():
    '''Display Program greeting'''
    print('~' * 60)
    print(format('Temperature Conversion Program', '^60'))
    print(format('Convert a range of temparatures', '^60'))
    print('~' * 60)
    print('Enter (F) to convert Fahrenheit to Celcius')
    print('Enter (C) to convert Celcius to Fahrenheit')
    print('~' * 60)

def get_conversion_type():
    '''Prompt user for Conversion Type.
    Fahreheit to Celcius & vice-versa
    '''
    selection = input('Enter selection (F/C): ').upper()
    while selection != "F" and selection != 'C': # Error-check
        selection = input('Enter selection (F/C): ')
    return selection

def display_fahren_to_celcius(start, end):
    '''convert a range of values from Fahrenheit to Celsius.'''
    print('\n')
    print(format('Degrees', '^12'), format('Degrees', '^12'))
    print(format('Fahrenheit', '^12'), format('Celcius', '^12'))
    
    for temp in range(start, end + 1):
        converted_temp = (temp - 32) * 5/9
        print(format(temp, '9.1f'), format(converted_temp, '9.1f'))

def display_celcius_to_fahren(start, end):
    '''convert a range of values from Celsius to Fahrenheit.'''
    print('\n')
    print(format('Degrees', '^12'), format('Degrees', '^12'))
    print(format('Celcius', '^12'), format('Fahrenheit', '^12'))

    for temp in range(start, end + 1):
        converted_temp = (9/5 * temp) + 32
        print(format(temp, '9.1f'), format(converted_temp, '9.1f'))

def convert_temp():
    '''convert a range of values from Fahrenheit to Celsius, 
    or Celsius to Fahrenheit.
    '''
    display_welcome() # Program Greeting
    which = get_conversion_type() # Assign Conversion Type
    
    # Prompt User for values
    proper_conversion_units = False

    while not proper_conversion_units: # Error-Check user input
        try:
            temp_start = int(input('Enter Starting temperature value to convert: '))
            temp_end = int(input('Enter Ending temperature value to convert: '))
            proper_conversion_units = True
        except ValueError:
            print('Expected integer')

    if which == 'F':
        display_fahren_to_celcius(temp_start, temp_end)
    else:
        display_celcius_to_fahren(temp_start, temp_end)

if __name__ == '__main__':
    convert_temp()