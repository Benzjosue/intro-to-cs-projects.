'''
Program name: Floating-point Normalizer
Author name: Benz Josue
Description: This program adjust the input calues by dividing all inputs
             by the latgest value
'''

num_of_values = int(input('Please enter the number of floating-point values:'))

float_list = []

for i in range(num_of_values): #range(end)
    user_floating_point = float(input('Please Enter a floating-point value: '))
    float_list.append(user_floating_point) #append evert input value to the list

max_float = max(float_list) #find the largest value in the list

print(' Normalized Floating-Point Values:')
for number in float_list:
    normalized_value = number / max_float
    print(f'{normalized_value:.2f}') # print the normalized value with 2 decimal places