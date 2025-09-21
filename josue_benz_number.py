'''
Program name: Number operations
Author name: Benz Josue
Description: This program perfroms special operations on integers
'''

class Number:
    def __init__(self,num):
        self.num = num
    
    def __str__(self):
        return str(self.num)
    
    def __add__(self, other):
        return Number(self.num + other.num)
    
    def __sub__(self, other):
        return Number(self.num - other.num)
    
    def __mul__(self, other):
        return Number(self.num * other.num)
    
    def __truediv__(self, other):
        return Number(self.num // other.num) # Integer division
    

num_a = Number(25)
num_b = Number(5)

print()
num_1 = num_a + num_b
print(f'{num_a} + {num_b} = {num_1}')
num_2 = num_a - num_b
print(f'{num_a} - {num_b} = {num_2}')
num_3 = num_a * num_b
print(f'{num_a} * {num_b} = {num_3}')
num_4 = num_a / num_b
print(f'{num_a} / {num_b} = {num_4}')
num_5 = (num_1 + num_2 * num_4) / num_3
print(f'{num_1} + {num_2} * {num_4} / {num_3} = {num_5}')
