import time

current_time = time.time()


def speed_calc_decorator(function):
    function()
    print(f"{function.__name__} run speed: {time.time() - current_time}")


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


"""
Decorators are syntactic sugar over below code
speed_cal_fast_function = speed_calc_decorator(fast_function)
speed_cal_fast_function()

speed_cal_slow_function = speed_calc_decorator(slow_function)
speed_cal_slow_function()

"""
# fast_function run speed: 0.6166119575500488
# slow_function run speed: 7.42035984992981
