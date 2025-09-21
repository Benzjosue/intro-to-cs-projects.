'''
Program name: Food Order Calculator
Author name: Benz Josue
Description: This program will store the menu items and their prices as a dictionary.
             The program will then calculate the total cost of the order.
'''
# Dictionaries: {'Key': Value, 'Key' : Value, ...}
# Access value from a dict: food_menu[]
food_menu = {'Hot Dog': 1.50, 'Slice of Pizza': 1.99, 'Whole Pizza': 9.95, 'Soft Drink': 0.59}

num_hot_dog = int(input('Please enter the number of Hot Dogs: '))
print()
num_slice_pizza = int(input('Please enter the number of Pizza Slices: '))
print()
num_whole_pizza = int(input('Please enter the number of Whole Pizzas: '))
print()
num_soft_drink = int(input('Please enter the number of soft drinks: '))
print()

total_cost = (num_hot_dog * food_menu['Hot Dog'] + num_slice_pizza * food_menu['Slice of Pizza']
            + num_whole_pizza * food_menu['Whole Pizza'] + num_soft_drink * food_menu['Soft Drink'])

print(f'The total cost of the order is ${total_cost:.2f}')