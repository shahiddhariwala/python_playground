# Write your code below this line 👇

def prime_checker(number):
    divisible_count = 0
    is_prime = True
    counter = 2
    while counter <= number:
        if number % counter == 0:
            divisible_count += 1
        counter += 1
    if divisible_count == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
