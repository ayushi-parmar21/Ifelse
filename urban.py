age=int(input("enter a age : "))
gender=input("enter a gender")
married=input("enter you merried")
if gender=="male":
	if age>=20 and age<=40:
		if married=="yes":
		      print("urban area")
		else :
			print("rural area")
if gender=="male":
	if age>=40 and age<=60:
		if married=="yes":
		      print("urban cab service")	    
if gender=="female":
	if age>=20 and age<=40:
		if married=="no":
		      print("rural area")
	if age>=40 and age<=60:
		if married=="yes":
			print("urban area")