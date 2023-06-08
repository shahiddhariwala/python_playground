# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}({args})")
        print(f"It returned: {function(*args)}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
