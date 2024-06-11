# A votung program to tst nationality and age
#kenyan citizen,  age above 18 years
age=int(input("Enter your age: "))
citizenship=input("Enter your nationality: ").lower()
if age>=18 and citizenship== "kenyan":
    print("Eligible to vote")
else:
    print("Not eligible to vote")