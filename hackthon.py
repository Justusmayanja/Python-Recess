# Creating my own exception for invalid inputs
class InvalidInputError(Exception):
    pass


# This decorator checks whether the inputs are numbers
def validate_inputs(func):
    def wrapper(a, b):
        try:
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise InvalidInputError("Inputs must be numbers.")

            result = func(a, b)

            # Save the operation and answer in a log file
            with open("log.txt", "a") as file:
                file.write(f"{func.__name__}({a}, {b}) = {result}\n")

            return result

        except InvalidInputError as e:
            print(e)

    return wrapper


# This decorator prevents the program from crashing when dividing by zero
def safe_divide(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Infinity"

    return wrapper


# Function for addition
@validate_inputs
def add(a, b):
    return a + b


# Function for subtraction
@validate_inputs
def subtract(a, b):
    return a - b


# Function for multiplication
@validate_inputs
def multiply(a, b):
    return a * b


# Function for division
@validate_inputs
@safe_divide
def divide(a, b):
    return a / b


# Testing section
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "5":
        print("Program ended.")
        break

    first = input("Enter first value: ")
    second = input("Enter second value: ")

    # Convert the inputs to numbers
    try:
        first = float(first)
        second = float(second)
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        print("Result:", add(first, second))

    elif choice == "2":
        print("Result:", subtract(first, second))

    elif choice == "3":
        print("Result:", multiply(first, second))

    elif choice == "4":
        print("Result:", divide(first, second))

    else:
        print("Invalid choice.")

