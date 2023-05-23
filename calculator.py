art = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def add(n1, n2):
    """
    Adds two numbers n1 + n2.

    Args:
        n1 (int): The first number to add.
        n2 (int): The second number to add.

    Returns:
        int: The sum of n1 and n2.
    """
    return n1 + n2


def subtract(n1, n2):
    """
    Subtracts two numbers n1 - n2.

    Args:
        n1 (int): The first number to subtract.
        n2 (int): The second number to subtract.

    Returns:
        int: The difference of n1 and n2.
    """
    return n1 - n2


def multiply(n1, n2):
    """
    Multiplies two numbers n1 * n2.

    Args:
        n1 (int): The first number to multiply.
        n2 (int): The second number to multiply.

    Returns:
        int: The product of n1 and n2.
    """
    return n1 * n2


def divide(n1, n2):
    """
    Divides two numbers n1 / n2.

    Args:
        n1 (int): The first number to divide.
        n2 (int): The second number to divide.

    Returns:
        float: The quotient of n1 and n2.
    """
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}


def calculator():

    print(art)
    num1 = float(input("What's first number?: "))

    should_continue = True
    for symbol in operations:
        print(symbol)

    while should_continue:
        operation = input("Please choose the operation: ")
        num2 = float(input("What's next number?: "))

        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"Do you want to continue to perform operation on {answer}, type 'Y' to continue or type 'N' to start new calculation\n").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


try:
    import os
    os.system("clear")
    calculator()
except ValueError:
    print("Please check your inputs should be either int or float")
except:
    print("Something went wrong, do check your input")
