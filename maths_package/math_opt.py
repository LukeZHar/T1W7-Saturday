# Using *args

def multiply(*args):
    multiply = 1
    for each in args:
        multiply *= each
    return multiply

def divide(a,b):
    if b == 0:
        return "Error! Divided by Zero"
    return a / b
