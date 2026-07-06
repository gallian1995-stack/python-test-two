def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("select operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    if choice in ('1', '2','3', '4'):
        num1 = float(input("enter first number:"))
        num2 = float(input("Enter second number: "))
        try:
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except ValueError:
            print("Error: Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice!")