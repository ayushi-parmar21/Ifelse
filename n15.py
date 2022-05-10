side1=int(input("enter the first side: "))
side2=int(input("enter the second side: "))
side3=int(input("enter the third side: "))
if (side1+side2>side3) or (side2+side3>side1) or (side1+side3>side2):
    print("Triangle is valid: ")
else :
    print("triangle is invalid: ")