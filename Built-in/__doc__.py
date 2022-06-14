def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

factorial.__doc__

# "returns n!" 이 출력됨
