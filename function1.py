
def myAddition(a, b):
    print("Add a to b")
    return a + b

def mySubtraction(a, b):
    print("Subtract a from b")
    return a - b

def myMultiplication(a, b):
    print("Multiply a with b")
    return a * b

def myDivision(a, b):
    print("Divide a by b")
    return a / b

def myMenu():
    print("Main Menu")
    print("1 > Addition operation")
    print("2 > Subtraction operation")
    print("3 > Multiplication operation")
    print("4 > Division operation")
    choice = int(input("Enter your choice: "))
    return choice

def calculation():
    ch = myMenu()
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    if ch == 1:
        print("Result:", myAddition(num1, num2))
    elif ch == 2:
        print("Result:", mySubtraction(num1, num2))
    elif ch == 3:
        print("Result:", myMultiplication(num1, num2))
    elif ch == 4:
        print("Result:", myDivision(num1, num2))
    else:
        print("Invalid choice")

calculation()
