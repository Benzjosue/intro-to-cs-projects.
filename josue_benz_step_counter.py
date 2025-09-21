'''
Program name: Step Counter
Author: Benz Josue
Descritption: This program counts the number of steps taken by a user and converts to miles.
'''

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        
def steps_to_miles(num_steps):
    if num_steps < 0:
        raise NegativeValueError('Exception: Negative Step Count Entered')
    miles = num_steps / 2000
    return miles
    
try:
    user_steps = int(input('Enter # of Steps:> '))
    user_miles = steps_to_miles(user_steps)
    print(f'{user_miles:.2f} miles.')
except ValueError:
    print('Exception: Non-Numeric Value Entered')
except NegativeValueError as e:
    print(e)


     