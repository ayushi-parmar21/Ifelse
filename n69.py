age1=int(input("enter the first side: "))
age2=int(input("enter the second side: "))
age3=int(input("enter the third side: "))
if age3>age2+age1:
    print("Triangle is obtus angle: ")
if age3==age2+age1:
    print("Triangle is right angle: ")
else :
    print("triangle is actual angel: ")