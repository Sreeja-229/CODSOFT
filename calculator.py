# Basic Calculator

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Display operation options
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Taking input from the user
choice = input("Enter choice (1/2/3/4): ")

# Check if the input choice is valid
if choice in ['1', '2', '3', '4']:
    # Prompt user for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform the selected operation
    if choice == '1':
        print(f"The result of {num1} + {num2} is {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of {num1} - {num2} is {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of {num1} * {num2} is {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of {num1} / {num2} is {divide(num1, num2)}")
else:
    print("Invalid input, please choose a valid operation.")
