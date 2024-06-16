def add(n1,n2):
    return n1 + n2

def calculate(add,n1,n2):
    return add(n1,n2)

"""
Functions are treated as first class objects,can be passed around as
arguments e.g. int,string,float etc.
"""

"""
nested function
"""

def outer_function():
    print("I am outer function")

    def nested_function():
        print("I am inner function")

    return nested_function
if __name__ == "__main__":
    result = calculate(add,3,4)
    print(result)
    nested = outer_function()
    print(nested())
