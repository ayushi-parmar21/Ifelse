ap=int(input("enter a actual product price"))
sp=int(input("enter a sale product price"))
if ap>sp:
    amount=ap-sp
    print("total loss amount: ",amount)
elif sp>ap:
    amount=sp-ap
    print("total profit amount: ",amount)
else:
    print("no profit no loss: ")