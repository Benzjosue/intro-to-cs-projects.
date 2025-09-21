'''
Program name: Speeding Ticket Calculator
Author name: Benz Josue
Description: This program takes two integers representing a speed limit 
             and driving speed in miles per hour (mph) and outputs
             the traffic ticket amount
'''

speed_limit = int(input('Please enter the speed limit for the road: '))
driving_speed = int(input("Please enter the vehicle's recorded speed: "))

if (driving_speed - speed_limit) <= -10:
    print("The speeding fine $50.")
elif 6 <= (driving_speed - speed_limit) <= 20:
    print("The speeding fine is $75.")
elif 21<= (driving_speed - speed_limit)<= 40:
    print('The speeding fine is $150.')
elif (driving_speed - speed_limit) > 40:
    print("The speeding fine is $300.")
else:
    print("There is no fine.")