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

'''
Yes, the modulo operation takes more computational power than other arithmetic operations, 
such as addition, subtraction, multiplication, and division. This is because the modulo operation requires 
the computer to perform a division operation, and then find the remainder of the division. 
The division operation is itself a relatively computationally expensive operation, and adding the 
additional step of finding the remainder makes the modulo operation even more expensive.

The amount of computational power required for the modulo operation depends on the size of the numbers
 being operated on. For small numbers, the difference in computational power may not be significant.
   However, for large numbers, the difference can be significant. For example, the modulo operation of
     two 64-bit numbers can take up to 10 times longer than the addition operation of the same two numbers.

The modulo operation is often used in cryptography and other applications where it is important to ensure 
that the results of an operation are not predictable. However, the increased computational cost of the modulo
 operation should be taken into account when designing algorithms that use this operation.
'''
