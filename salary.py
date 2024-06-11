# programm to calculate the bonus
salary=int(input("Enter your salary"))
year=int(input("Number of years:"))
if year <=6:
    bonus=salary*10/100
    print(bonus)
elif year >=6 and year <=10:
    bonus=salary*8/100
    print(bonus)
else:
    bonus=salary*5/100
    print(bonus)