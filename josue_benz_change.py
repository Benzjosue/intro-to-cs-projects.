'''
Program name: Change Calculator 
Author name: Benz Josue
Description: This program converts a user-entered number of cents 
             into the fewest number number of US coins of that amount.
'''

user_cents = int(input('please enter a number of cents')) #98
quarters = user_cents // 25 #3 98-75 = 23

user_cents = user_cents - (quarters*25) # update the user_cents

dimes = user_cents // 10 # = 2 remainder is 3 
user_cents -= dimes*10 #3
nickels = user_cents // 5 # =0 remainder is 3
user_cents -= nickels*5 #3
pennies = user_cents # =3 

print(f'Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies ')

