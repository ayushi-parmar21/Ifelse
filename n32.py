unit=int(input("enter "))
if unit<=100:
	charge=0
	print("no charge")
elif unit>100 and unit<=200:
	charge=(unit-100)*5
	print("unit",charge)
elif unit>200:
	charge=(unit-200)*10+500
	print("unit",charge)