def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

print(factorial.__doc__)

# "returns n!" 이 출력됨

def square_root(x):
    """Returns the square root of the argument x"""
    return x ** 0.5 

print(square_root.__doc__)

# message가 출력
