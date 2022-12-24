import math
#simple interest . si 
def sii(x, y, z):
    return ((x*y*z)/100)

#simple interest . amount
def sia(x, y, z):
    return (x+((x*y*z)/100))

#compound interest . ci
def cii(x, y, z):
    r=(pow(((100+y)/100),z)) 
    return ((x*r)-x)

#compound interest . amount
def cia(x, y, z):
    r=(pow(((100+y)/100),z)) 
    return (x*r)

while True:
    # take input from the user
    choice = input("""Select operation:
1.Find Simple Interest(si)
2.Find Compound Interest(ci)
3.Find Simple Interest(amount)
4.Find Compound Interest(amount)
Enter choice(1/2/3/4): """)

    # check if choice is one of the five options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter Principle number: "))
        num2 = float(input("Enter Rate number: "))
        num3 = float(input("Enter Time number: "))

        if choice == '1':
            print("Simple Interest(si) = ",sii(num1, num2, num3))

        elif choice == '2':
            print("Compound Interest(ci when compounnde annually) = ",cii(num1, num2, num3))

        elif choice == '3':
            print("Simple Interest(amount) = ",sia(num1, num2, num3))

        elif choice == '4':
            print("Compound Interest(amount when compounnde annually) = ",cia(num1, num2, num3))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("continue? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
