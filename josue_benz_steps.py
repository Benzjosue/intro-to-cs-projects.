'''
Program name: Distance to Step Converter
Author name: Benz Josue
Description:  this program converts a distance in feet from user to steps.

'''

def feet_to_steps(distance):
    #parameter(s): distance, is a float representing in feet
    steps = distance / 2.5
    return int(steps)
if __name__ == '__main__':
    user_distance = float(input('Please enter the distance traveled in feet: '))
    user_steps = feet_to_steps(user_distance)
    print(f'{user_steps} steps')