'''
Program name:
Author name:
Description: This program determines whether a given character is a 
             vowel, consonant, or punctuation.
'''
vowels = ['a', 'e', 'i','o','u']
digits = [ '0','1','2','3','4','5','6','7','8','9']
punctuation = [',',';','-','?','!']

character = input('Please enter a character: ')
character = character.lower() # convert to lowercase

if character in vowels:
    print(f'The character "{character} is a vowel')
elif character in digits:
    print(f'The character "{character}" is a digit.')
elif character in punctuation:
    print(f'The character "{character} is punctuation.')
else:
    print(f'The character "{character} is a consonant.')