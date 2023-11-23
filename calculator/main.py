from calc_art import logo
print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Division
def division(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
              }


def calculator():
    num1 = int(input("What's the first number?: "))
    for key in operations:
        print(key)
    is_exit = False
    while not is_exit:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        is_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if is_continue == 'y':
            num1 = answer
        else:
            is_exit = True
            calculator()


calculator()