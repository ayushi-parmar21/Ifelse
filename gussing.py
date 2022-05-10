guess=8
print("guess between (1,10)")
num=int(input("guess the number"))
if num==guess:
	print("you are guessing is exactly right")
elif num>guess:
	print("smaller than you print")
else :
	print("greater than you print")