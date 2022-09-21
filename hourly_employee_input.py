'''
Program: hourly_employee_input.py
Author: Joshua M McGinley
Last Date Modified: 09/21/2022

This program includes a function that takes name (string), hours worked (int), and hourly pay rate (float) as input
and prints a string of that information.

Open the editor of your choice. Write a function called hourly_employee_input that asks the user for a name (string), hours worked (int) and an hourly pay rate (float) and prints a string including the information. Include a docstring as your first line declaring what the function does.

    Run the script in a shell.
    Call the function, entering expected values, numbers in appropriate range
    Call the function, entering negative numbers
    Call the function, entering bad input (letters, symbols)
    What do you need to add to your function for bad input? Handle the bad input
'''
def hourly_employee_input():
    '''a function that takes name (string), hours worked (int), and hourly pay rate (float) as input
    and prints a string of that information.'''

    name = str(input('Enter name: '))
    try:
        hrs_worked = int(input('Enter hours worked: '))
    except:
        print('Evil input!')
    try:
        hr_rate = float(input('Enter hourly pay rate: '))
    except:
        print('Evil input!')

    try:
        print(name, hrs_worked, hr_rate)
    except:
        print('Bad, bad, bad!')

#driver code
if __name__ =="__main__":
    hourly_employee_input()

