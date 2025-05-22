# Get the maths library for higher operations
import math 

# Define functions for various mathematical operations
def add(x, y): 
    return x + y
def subtract(x, y): 
    return x - y
def multiply(x, y): 
    return x * y
def dividequo(x, y): 
    return x / y
def dividerem(x, y): 
    return x % y
def power(x, y): 
    return math.pow(x, y)
def sqrt(x, y): 
    return math.sqrt(x) if x >= 0 else 'Error: negative root'
def log(x, y): 
    return math.log10(x) if x > 0 else 'Error: log of non-positive'

# Using dictionary to optimist looping
operations = {
    '1': ('Add', add),
    '2': ('Subtract', subtract),
    '3': ('Multiply', multiply),
    '4': ('Divide (Quotient)', dividequo),
    '5': ('Divide (Remainder)', dividerem),
    '6': ('Power', power),
    '7': ('Square Root', sqrt),
    '8': ('Logarithm base 10', log),
}

# Rounding off large decimal values to the nearest 3th decimal
def format_result(result):
    if isinstance(result, float):  # Check if it's a float fot the current runtime instance
        return round(result, 3)  # Round to 3rd decimal
    return result

while True:
    # take key from the dictionary and its respective operation
    print("\nSelect operation:")# \n ensures new loop begins with a fresh line
    for key in operations:
        print(key + ". " + operations[key][0])

    choice = input("Enter choice (1/2/3/4/5/6/7/8): ").strip()# the .strip ensure that any extra spacings gets removed

    if choice in operations:
        try:
            # Handle different input requirements for operations
            if choice in ['7', '8']:  # Only one number required for sqrt and log
                num1 = float(input("Enter number: "))
                num2 = 0  # Placeholder, as we don't need the second number
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # From the dictionary, first bracket take the name while the second takes its funciton
        op_name = operations[choice][0]# Returns the name
        op_func = operations[choice][1]# Retuens the operation

        # Check for division by zero
        if op_func in [dividequo, dividerem] and num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = op_func(num1, num2)
            rounded_result = format_result(result)  # Get the rounded result if needed

            # Display normal and rounded results
            print(f"{op_name} result: {result}")
            if isinstance(result, float):
                print("Rounded result: " + str(rounded_result))

        # Continue or exit
        next_calculation = input("Continue? (yes/no): ").strip().lower()
        if next_calculation != "yes":
            print("Goodbye!")
            break
    else:
        print("Invalid input. Please enter a number from the menu.")
