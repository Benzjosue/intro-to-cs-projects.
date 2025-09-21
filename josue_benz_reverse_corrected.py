'''
Program name: String Reverser
Author name: Benz Josue
Description: This progtam takes in aline of text as input and outputs
             that line of text in reverse.
'''
while True:
    user_input = input('Please Enter Your String: ') # a string
    if user_input == 'Quit'or user_input == 'quit' or user_input == 'q':
        break

    reversed_string = '' # an empty string

    last_letter_index = len(user_input) - 1

    for i in range(last_letter_index, -1, -1): # range(start,end,step)
        reversed_string += user_input[i]

    print('Reversed:', reversed_string)
    
