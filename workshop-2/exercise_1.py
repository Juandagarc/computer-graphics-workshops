# Exercise 1: Basic Calculator
# Objective: Create functions for basic arithmetic operations and a main function to interact with the user

def add(a, b):
    """Function to add two numbers"""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers"""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers"""
    return a * b

def divide(a, b):
    """Function to divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator():
    """Main calculator function"""
    print("=== BASIC CALCULATOR ===")
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        print("\nAvailable operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation_choice = input("Select an operation (1-4): ")

        if operation_choice == "1":
            result = add(first_number, second_number)
            print(f"\n{first_number} + {second_number} = {result}")
        elif operation_choice == "2":
            result = subtract(first_number, second_number)
            print(f"\n{first_number} - {second_number} = {result}")
        elif operation_choice == "3":
            result = multiply(first_number, second_number)
            print(f"\n{first_number} × {second_number} = {result}")
        elif operation_choice == "4":
            result = divide(first_number, second_number)
            print(f"\n{first_number} ÷ {second_number} = {result}")
        else:
            print("Invalid operation")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
