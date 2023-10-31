import math 

def add(a, b):
    return a+ b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def exp(a, b):
    return (pow(a, b))


def sqrt(a):
    return (math.sqrt(a))

def log(a,b):
    return math.log(a,b)

def ln(a):
    return(math.log(a))

def modulus(a, b): 
    return(math.remainder(a, b))

def sin(a):
    return(math.sin(a))

def cos(a):
    return(math.cos(a))

def tan(a):
    return(math.tan(a))

# def clear(a, b):
#         a=0
#         b=0
#         return "the variables have been cleared"

def calculator():
    while True:
        print("Options:add, subtract, multiply, divide, exponent, sqrt, log, ln, modulus, sin, cos, tan, clear")
        user_input = input(": ")

        # if user_input == "clear":
        #     clear(a,b)
        if user_input == "add":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))
        elif user_input == "subtract":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))
        elif user_input == "multiply":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply(a, b))
        elif user_input == "divide":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", divide(a, b))
        elif user_input == "exponent":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", exp(a, b))
        elif user_input == "sqrt":
            a = float(input("Enter a number: "))
            print("Result:", sqrt(a))
        elif user_input == "log":
            a = float(input("Enter a number: "))
            b = float(input("Enter a base: "))
            print("Result:", log(a,b))
        elif user_input == "ln":
            a = float(input("Enter a number: "))
            print("Result:", ln(a))
        elif user_input == "modulus":
            a = float(input("Enter dividend: "))
            b = float(input("Enter divisor: "))
            print("Result:", modulus(a, b))
        elif user_input == "sin":
            a = float(input("Enter a number: "))
            print("Result:", sin(a))
        elif user_input == "cos":
            a = float(input("Enter a number: "))
            print("Result:", cos(a))
        elif user_input == "tan":
            a = float(input("Enter a number: "))
            print("Result:", tan(a))
        else:
            print("Invalid input. Please try again.")

calculator()
