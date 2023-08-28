#Learn to make a simple python calculator

repeat = True
while repeat == True:
    print("Welcome to the calculator!")
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice : ")
    
    def input_number():
        num1 = float(input("Enter first number  : "))
        num2 = float(input("Enter second number : "))
        return num1, num2

    def sum(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1*num2

    def divide(num1, num2):
        return num1/num2
    
    def continuing(check):
        if check != "y":
            repeat = False
            return repeat

    if choice == "1":
        a,b = input_number()
        print("sum result : "+ str(sum(a, b)))
        print("Do you want to continue? (y/n)")
        continuing()
    elif choice == "2":
        a, b = input_number()
        print("subtract result : "+ str(subtract(a, b)))
        check = input("Do you want to continue? (y/n) : ")
        repeat = continuing(check)
    elif choice == "3":
        a, b = input_number()
        print("multiply result : "+ str(multiply(a, b)))
        print("Do you want to continue? (y/n)")
        continuing()
    elif choice == "4":
        a, b = input_number()   
        print("divide result : "+ str(divide(a, b)))
        print("Do you want to continue? (y/n)")
        continuing()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
        print("Do you want to continue? (y/n)")
        continuing(check)
    
print("Thank you for using my simple the calculator!")
