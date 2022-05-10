mark=int(input("enter your marks"))
if mark<=25:
	print("grade F")
elif mark>=25 and mark<=45:
	print("grade E")
elif mark>=45 and mark<=50:
	print("grade D",)
elif mark>=50 and mark<=60:
	print("grade C",)
elif mark>=60 and mark<=80:
	print("grade B",)
else:
    print("grade A")