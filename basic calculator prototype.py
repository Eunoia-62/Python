#add
def add(x, y):
    return x + y

#subtract
def subtract(x, y):
    return x - y

#multiply
def multiply(x, y):
    return x * y

#divide for quotient
def dividequo(x, y):
    return x / y

#didive for reminder
def dividerem(x, y):
    return x % y

while True:
    # take input from the user
    choice = input("""Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide(Quotient)
5.Divide(Reminder)
Enter choice(1/2/3/4/5): """)

    # check if choice is one of the five options
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("sum = ",add(num1, num2))

        elif choice == '2':
            print("difference = ",subtract(num1, num2))

        elif choice == '3':
            print("product = ",multiply(num1, num2))

        elif choice == '4':
            print("quotient = ",dividequo(num1, num2))
            
        elif choice == '5':
            print("reminder = ",dividerem(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("continue? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
