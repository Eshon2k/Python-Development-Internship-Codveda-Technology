# Calculator for Codveda Technology: Addition, Subtraction, Multiplication, Division
# Handles division by zero with error messages

def add(x, y):
    return x + y  # Return sum of x and y

def subtract(x, y):
    return x - y  # Return difference of x and y

def multiply(x, y):
    return x * y  # Return product of x and y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."  # Handle division by zero
    return x / y  # Return quotient of x and y

def calculator():
    print("Welcome to Codveda Technology Calculator!")  # Welcome message

    while True:
        # Display menu options
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")  # Option to exit

        choice = input("Enter choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")  # Exit message
            break  # Exit the loop to end program

        if choice in ('1', '2', '3', '4'):
            try:
                # Get user input for numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")  # Handle non-numeric input
                continue  # Restart loop

            # Perform operation based on choice
            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):  # Check if error message
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid option.")  # Handle invalid menu choice

# Run the calculator
if __name__ == "__main__":
    calculator()
