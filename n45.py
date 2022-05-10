day=int(input("enter a day: "))
if day<=5:
    amt=day*2
elif day>=6 and day<=10:
    amt=day*3
elif day>10 and day<=15:
    amt=day*4
else:
    amt=day*5
print("enter total amount: ",amt)