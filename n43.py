age=int(input("enter number of age"))
sex=input("enter sex")
nd=int(input("enter number of days"))
if age>=18 and age<30:
	if sex=="male":
		amt=nd*700
		print("total weges:",amt)
	else :
		amt=nd*750
		print("total weges:",amt)
if age>=30 and age<=40:
	if sex=="male":
		amt=nd*800
		print("total weges:",amt)
	else :
		amt=nd*850
		print("total weges:",amt)
else :
	print("appropriate")