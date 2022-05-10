salary=int(input("enter your salary: "))
year=int(input("enter year of working: "))
if year>=5:
    s=salary+salary*5/100
    print("bonus is: ",s)
else:
    print("No bonus: ",salary)