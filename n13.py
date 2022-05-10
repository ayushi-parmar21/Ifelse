amount=int(input("enter the amount: "))
Option=int(input("enter the option: "))
if Option==1:
    result=amount//500
    print("number of 500 notes: ",result)
elif Option==2:
    result=amount//200
    print("number of 200 notes: ",result)
elif Option==3:
    result=amount//100
    print("number of `100 notes: ",result)
elif Option==4:
    result=amount//50
    print("number of 50 notes: ",result)
elif Option==5:
    result=amount//10
    print("number of 10 notes: ",result)
elif Option==6:
    result=amount//1
    print("number of 1 notes: ",result)
else:
    print("only 1 to 6 option avaliable")