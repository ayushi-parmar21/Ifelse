month=input("enter the num")
if month=="February":
	print("number of days:28/29 days")
elif month in("April","june","september","novber"):
    print("number of days:30 days")
elif month in("january","march","may","july","august","octomber","december"):
    print("number of days:30 days")
else:
    print("wrong month name")