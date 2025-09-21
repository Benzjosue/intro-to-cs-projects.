'''
Program name: Number Guessing Game
Author name: Benz Josue
Description: This porgram allows the user to guess a randomly generated number
'''
import random

random_number = random.randint(1,100)
print('I have generated random number between 1 and 100. you wil have 10 attempts to guess that number.')

for i in range(10):
    guess = int(input(f'Guess {i + 1}:'))
    if guess == random_number:
        print('You correctly guessed my random number!')
        break
    elif guess < random_number:
        print('Your guess is less than my random number. Try Again ')
    else:
        print("Your guess is geater than my random number. Try again.")
else: #only executes if the whole for loop is iterated without a break
    print("you have used all of your 10 attempts. Sorry!")