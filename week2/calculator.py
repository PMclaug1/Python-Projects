import art3

#calculator

#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1/n2

#calc functions dictionary
calc_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

for operation in calc_functions:
    print(operation)

operation_symbol = input("Pick an operation from the line above.")

calc_funct = calc_functions[operation_symbol]

answer = calc_funct(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
