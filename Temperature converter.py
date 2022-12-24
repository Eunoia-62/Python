#cel to fah
def cel(x):
	return (((x*9)/5)+32)

#fah to cel
def fah(x):
	return (((x-32)*5)/9)

while True:
    # take input from the user
    choice = input("""Select operation:
1.Celsius To Fahrenheit
2.Fahrenheit To Celsius
Enter choice(1/2): """)

    # check if choice is one of the two options
    if choice in ('1', '2'):
        num = float(input("Enter degree: "))

        if choice == '1':
            print("Fahrenheit = ",cel(num))

        elif choice == '2':
            print("Celsius = ",fah(num))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("continue? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


