from calculator.operation import add,subtract,multiply,divide
# command-line-calculator/main.py
# This is a simple command line calculator that performs basic arithmetic operations.

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to the Command Line Calculator!")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'q' to quit the calculator.")

    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    while True:
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
        if operation == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        if operation not in operations:
            print("Invalid operation. Please try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = operations[operation](num1, num2)
            print(f"The result of {operation} between {num1} and {num2} is: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}. Cannot divide by zero.")

if __name__ == "__main__":  
    main()