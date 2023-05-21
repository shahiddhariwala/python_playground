for number in range(1, 101):
    is_div_by_3 = number % 3 == 0
    is_div_by_5 = number % 5 == 0

    if is_div_by_5 and is_div_by_3:
        print("FizzBuzz")
    elif is_div_by_5:
        print("Buzz")
    elif is_div_by_3:
        print("Fizz")
    else:
        print(number)
