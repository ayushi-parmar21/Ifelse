ch=input("enter the character")
if ch>="a" and ch<="z":
	print("alphabet",ch)
if ch>="A" and ch<="Z":
	print("alphabet",ch)
elif ch>="0" and ch<="9":
	print("digit",ch)
else:
	print("special character",ch)