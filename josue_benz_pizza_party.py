"""
Program name: Interest
Author name: Benz Josue
Description: This program prints the total area of pizza and total area per slice
"""
# Get user input for number of people, pizzas, diameter,slices per pizza.
people = int(input('Please enter the number of people attending the party: '))
pizza = int(input('Please enter the number of pizzas purchased for the party: '))
diameter = int(input('please enter the diameter of the pizzas: '))
slices = int(input('please enter the number of slices per pizza: '))
#calculations 
totalarea = pizza*3.14*(diameter/2)**2
totalslices = slices*pizza
slicesperson = (slices*pizza)/people
areaperperson = round((pizza*3.14*(diameter/2)**2)/people,2)
#display the results
print('Total pizza area: ',totalarea, 'square inches')
print('Total number of slices',totalslices)
print('Pizza area per person: ',areaperperson, 'square inches')
print('Slices per person: ',slicesperson,)