# a program to add, subtruct, devide and multiply two numbers
def myAddition(a,b):
    ptint("Add a to b")
    return(a+b)
def mySubtruction(a,b):
    ptint("Subtruct  a from b")
    return(a-b)
def myMultiplication(a,b):
    ptint("Multiply  a with b")
    return(a*b)
def myDivision(a,b):
    ptint("Devide  a with b")
    return(a/b)
def myMenu():
    print("Main Menu")
    print("1>Addition operation")
    print("2>Subtruction operation")
    print("3>Multiplication operation")
    print("4>Division operation")
    return choice
def calculation():
    ch = myMenu()
    num1 = int(input("Please enter the first number"))
    num2 = int(input("Please enter the second number"))
    if ch == 1:
        output = myAddition(num1, num2)
    elif ch == 2:
        output = mySubtruction(num1, num2)
    elif ch == 3:
        output = myMultiplication(num1, num2)
    elif ch == 4:
        output = myDivision(num1, num2)
print("Answer =",output)
calculation()
