# Simple Calculator App

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):

    if num2 == 0:
        return "Cannot divide by zero"

    return num1 / num2


print("================================")
print("      PYTHON CALCULATOR")
print("================================")

while True:

    print("\nChoose an operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            answer = add(num1, num2)
            print("Answer =", answer)

        elif choice == "2":
            answer = subtract(num1, num2)
            print("Answer =", answer)

        elif choice == "3":
            answer = multiply(num1, num2)
            print("Answer =", answer)

        elif choice == "4":
            answer = divide(num1, num2)
            print("Answer =", answer)

    except ValueError:
        print("Please enter valid numbers.")