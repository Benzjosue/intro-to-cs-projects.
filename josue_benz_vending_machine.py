'''
Program name: Vending Machine
Author name: Benz Josue
Descrption: This program simulates a vending machine that allows users to
            select items to buy or to restock, and reports the inventory.

'''

class VendingMachine:
    def __init__(self, soda, water, coffee):
        self.soda = soda
        self.water = water
        self.coffee = coffee

    def purchase(self,type):
        if type == 1:
            self.soda -= 1
        elif type == 2:
            self.coffee -= 1
        elif type == 3:
            self.water -= 1 

    def restock(self,type,amount):
        if type == 1:
            self.soda += amount
        elif type == 2:
            self.coffee += amount
        elif type == 3:
            self.water += amount
    
    def report(self):
        print('Inventory')
        print(f'Soda: {self.soda} bottles')
        print(f'Coffee: {self.coffee} bottles')
        print(f'Water: {self.water} bottles')

my_machine = VendingMachine(10,10,10)

while True: 
    initial_input = input(":> ")
    if initial_input == 'quit' or initial_input == "q":
        break
    elif initial_input == "buy":
        print()
        print('Please select an option\n1 - Soda\n2 - Coffee\n3 - Water\n')
        choice = int(input(':> '))
        my_machine.purchase(choice)
    elif initial_input == "restock":
        print()
        print('Please select an option\n1 - Soda\n2 - Coffee\n3 - Water\n')
        choice = int(input (':> '))
        print('\n Please enter an amount: ')
        amount = int(input(':> '))
        my_machine.restock(choice, amount)
    elif initial_input == 'inventory':
        print()
        my_machine.report()
        print()
