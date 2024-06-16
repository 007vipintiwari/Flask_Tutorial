import time

def delayed_function(function):
    def wrapper_function():
        time.sleep(5)
        function()
        function()

    return wrapper_function

"""
option 1 of using decorators
"""
def say_hello():
    print("Hello")

delay = delayed_function(say_hello)
print(delay())


"""
option 2 of using decorators
"""

@delayed_function
def say_namaste():
    print("Namaste Duniya")

say_namaste()