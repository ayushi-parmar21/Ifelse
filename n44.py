a=int(input("enter the first num"))
b=int(input("enter the second num"))
c=int(input("enter the third num"))
if a>b and a<c or a<b and a>c:
	print("middle num is",a)
elif b>c and b<a or b<c and b>a:
	print("middle num is",b)
elif c>b and c<a or c<b and c>a:
	print("middle num is",c)