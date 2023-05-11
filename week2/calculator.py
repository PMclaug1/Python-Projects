import art3

# calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1/n2

# Exponent
def exponent(n1,n2):
    return n1**n2


# calc functions dictionary
calc_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent
}


def calculator():
    print(art3.logo)
    num1 = float(input("What is the first number? "))

    for operation in calc_functions:
        print(operation)

    continuation = True

    while continuation:
        operation_symbol = input("Pick an operation. ")
        calc_funct = calc_functions[operation_symbol]
        num2 = float(input("What is the next number? "))
        answer = calc_funct(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(
            f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation. Type 'exit' to quit. ").lower()
        if should_continue == "y":
            continuation = True
            num1 = answer
        elif should_continue == "n":
            continuation = False
            calculator()
        else:
            break
            


calculator()
