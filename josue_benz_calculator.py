"""
Program name: Terminal Calculator
Description: A simple calculator that handles basic math operations
Author: Benz Josue
"""

# Math Functions
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return None  # Can't divide by zero
    else:
        return x / y

def modulo(x,y):
    if y == 0:
        return None  # Can't divide by zero
    else:
        return x % y

def floordiv(x,y):
    if y == 0:
        return None  # Can't divide by zero
    else:
        return x // y

def power(x,y):
    return x ** y

def calculator():


    while True:
        user_expression = input("Please enter an Expression\n:> ")
        original_expression = user_expression.strip()
        expr_no_spaces = user_expression.replace(' ', '')
        # Quit logic
        if original_expression.lower() in ["q", "quit"]:
            break

        operators = ["**", "//", "+", "-", "*", "/", "%"]
        for operator in operators:
            if operator in expr_no_spaces:
                selected_operator = operator
                split_result = expr_no_spaces.split(operator)
                break
        else:
            print(f"Error: Invalid Expression - ({original_expression})\n")
            continue

        try:
            x = float(split_result[0])
            y = float(split_result[1])
        except (ValueError, IndexError):
            print(f"Error: Invalid Expression - ({original_expression})\n")
            continue

        # Division/modulo/floordiv by zero check
        if selected_operator in ["/", "%", "//"] and y == 0:
            print(f"Error: Invalid Expression - ({original_expression})\n")
            continue

        # Calculate and print result in required format
        if selected_operator == "+":
            result = add(x, y)
        elif selected_operator == "-":
            result = subtract(x, y)
        elif selected_operator == "*":
            result = multiply(x, y)
        elif selected_operator == "/":
            result = divide(x, y)
        elif selected_operator == "%":
            result = modulo(x, y)
        elif selected_operator == "//":
            result = floordiv(x, y)
        elif selected_operator == "**":
            result = power(x, y)

        print(f"Result: {x:g} {selected_operator} {y:g} = {result}\n")

calculator()



        