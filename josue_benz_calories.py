'''
Program name: calories calculator
Author name: Benz Josue
Description: This program estimates the average calories burned for a person when exercising.

'''

age = int(input('Please enter your age: '))
weight = int(input('Please enter your weight: '))
heart_rate = int(input('please enter your heart rate in beats per minute: '))
time = int(input('Please enter the length of your workout in minutes: '))

calories = (age*0.2757+weight*0.03295+heart_rate*1.0781-75.4991)*time/8.368

print(f'calroies burned: {calories:.2f} calories')