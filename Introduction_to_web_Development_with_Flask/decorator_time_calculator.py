import time
current_time = time.time()
def speed_cal_decorator(function):
    def wrapper_function():
        before = time.time()
        function()
        after = time.time()
        print(f"{function} run speed is : {after - before}")

    return wrapper_function

@speed_cal_decorator
def fast_function():
    for i in range(1000000):
        i = i*i

@speed_cal_decorator
def slow_function():
    for i in range(100000000):
        i = i * i



fast_function()
slow_function()