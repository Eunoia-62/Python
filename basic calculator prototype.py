# Define operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def dividequo(x, y): return x / y
def dividerem(x, y): return x % y

# Mapping of menu choices to operations and labels
operations = {
    '1': ('Add', add),
    '2': ('Subtract', subtract),
    '3': ('Multiply', multiply),
    '4': ('Divide (Quotient)', dividequo),
    '5': ('Divide (Remainder)', dividerem)
}

while True:
    # Show operation menu
    print("\nSelect operation:")
    for key in operations:
        print(key + ". " + operations[key][0])

    choice = input("Enter choice (1/2/3/4/5): ").strip()

    if choice in operations:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        op_name = operations[choice][0]
        op_func = operations[choice][1]

        # Check for division by zero
        if op_func in [dividequo, dividerem] and num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = op_func(num1, num2)
            print(op_name + " result = " + str(result))

        # Continue or exit
        next_calculation = input("Continue? (yes/no): ").strip().lower()
        if next_calculation != "yes":
            print("Goodbye!")
            break
    else:
        print("Invalid input. Please enter a number from the menu.")
