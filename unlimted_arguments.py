def calculate(*args):
    return sum(args)


def calulate_multiply(a, b=1, *args):
    mul = a * b
    # args is tuple type
    for num in args:
        mul *= num
    return mul


def divide_calculator(**kwargs):
    # kwargs is dict type

    return kwargs.get("numerator") / kwargs.get("denominator")


def mix_calculate(a=1, b=2, *args, **kwargs):
    return a + b + sum(args) + kwargs.get("z")


print(mix_calculate(1, 2, 3, 4, 5, 6, 7, z=-27))
# 1
print(divide_calculator(numerator=200, denominator=40))
# 5.0
print(calulate_multiply(1, 2, 3))
print(calulate_multiply(1, 2, 3, 5, 6))
# 6
# 180

print(calculate(1, 2, 3, 4))
print(calculate(1, 2, 3, 4, 6, 7, 8, 8))
print(calculate(1, 2, 3, 4, 56, 7, 7, 7))
# 10
# 39
# 87
