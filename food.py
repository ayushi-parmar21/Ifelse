day=input("enter the day")
time=input("enter the meal time")
if day=="monday":
	if time=="breakfast":
		print("poori sabzi")
	elif time=="lunch":
		print("sambhar rice")
elif day=="tuesday":
	if time=="breakfast":
		print("poha")
	elif time=="lunch":
		print("rajma rice")
	elif time=="dinner":
		print("roti dal")
else:
	print("nothing")