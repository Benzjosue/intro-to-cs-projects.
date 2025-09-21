'''
Program name: Phone Formatter
Author name: Benz Josue
Description: This program formats a given phone number as input
'''
phone_input = int(input("Please enter your phone number: "))
area_code = phone_input // 10000000

mid_three_operator = phone_input // 10000 #800555

mid_three = mid_three_operator % 1000 #555

last_four = phone_input % 10000 #1212


print('phone number: (' + str(area_code) +')' + str(mid_three) + '-' + str(last_four))