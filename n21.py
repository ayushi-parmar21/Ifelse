quantity=int(input("enter a quantity"))
if quantity>1000:
    dis=quantity-(quantity*10/100)
    print("cost is: ",dis)
else:
    print("cost is: ",quantity*100)