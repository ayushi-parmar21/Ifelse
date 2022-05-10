price=int(input("enter your basic salary"))
if price>100000:
    tax=price*15/100
elif price>50000 and price<=100000:
    tax=price*10/100
else:
    tax=price*5/100
print("tax to be paid: ",tax)