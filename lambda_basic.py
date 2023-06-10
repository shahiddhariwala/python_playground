check_even = lambda num: num % 2 == 0
multiply_by_2 = lambda num: num*2
check_number = lambda num: "Even" if num % 2 == 0 else "Odd"
for num in range(1, 101):
    print(check_even(num),check_number(num),f"{num} x 2 = " , multiply_by_2(num), )





    
