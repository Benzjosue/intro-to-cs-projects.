'''
Program name: Password Enchancer
Author name: Benz Josue
Description: This prgram strengthen a simple password 
             by replacing characters using the special keys
             and appedning "!" to the end of the input string.

'''

user_password = input('Please Enter yYour Password: ') # a string

new_password = '' # an empy string
for letter in user_password:
    if letter == 'o':
        new_password += '0'
    elif letter == 'i':
        new_password += '1'
    elif letter == 'a':
        new_password += '@'
    elif letter == 'e':
        new_password += '3'
    elif letter == 'A':
        new_password += '4'
    elif letter == 'B':
        new_password += '8'
    elif letter == 's':
        new_password += '$'
    else:
        new_password += letter
new_password += "!"

print('Your new strong password is:,', new_password)
