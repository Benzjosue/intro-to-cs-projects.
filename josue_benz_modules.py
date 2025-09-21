'''
Program name: Modules
Author name: Benz Josue
Description: This program will:
            1. Caluclate the volume of a Spehere
            2. Calculate the factorieal of a randomly generated number
'''
import math
import random

# Volume Calculation
radius = int(input('Please enter the radius of a spehere: '))
volume = (4/3)*math.pi*math.pow(radius, 3)
print(f'The volume of a sphere with radius of {radius} is {volume:.2f}')

# Factorial Calulation
random_number = random.randint(1,10)
factorial = math.factorial(random_number)
print(f'The factorial of {random_number} is {factorial}')