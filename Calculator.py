#learn to make a simple calculator
def input_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    print("Welcome to the calculator!")
    operations = {
        "1": ("sum", add),
        "2": ("subtract", subtract),
        "3": ("multiply", multiply),
        "4": ("divide", divide)
    }

    while True:
        print("Select an operation:")
        for key, value in operations.items():
            print(f"{key}. {value[0].capitalize()}")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "5":
            print("Thank you for using the calculator!")
            break
        
        if choice in operations:
            operation_name, operation_function = operations[choice]
            num1, num2 = input_numbers()
            result = operation_function(num1, num2)
            print(f"{operation_name} result: {result}")
        else:
            print("Invalid choice")
        
        check = input("Do you want to continue? (y/n): ")
        if check.lower() != "y":
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()
