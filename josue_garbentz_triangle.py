'''
Author: Benz Josue
Program: example 
Description: It calculates the perimeter and area using Heron's formula, 
             and determines whether the triangle is right, acute, or obtuse.
'''

import math  # We use this to calculate square roots

# Get user input
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Sort the sides so that c is the longest side
if a > b and a > c:
    a, c = c, a
elif b > c:
    b, c = c, b

# Calculate the perimeter
perimeter = a + b + c
print(f'The perimeter of the triangle is {perimeter:.0f}m')

# Calculate the semi-perimeter
s = perimeter / 2

# Use Heron's formula to calculate the area
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f'The area of the triangle is {area:.2f}m^2')

# Check what type of triangle it is
a_squared = a ** 2
b_squared = b ** 2
c_squared = c ** 2

if c_squared == a_squared + b_squared:
    print("It is a Right Triangle.")
elif c_squared < a_squared + b_squared:
    print("It is an Acute Triangle.")
else:
    print("It is an Obtuse Triangle.")
