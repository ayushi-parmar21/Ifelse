physics=int(input("enter physics marks"))
biology =int(input("enter biology marks"))
chemistry=int(input("enter chemistry marks"))
mathematics =int(input("enter mathematics marks"))
computer=int(input("enter computer marks"))
percentage=(computer+physics+biology+chemistry+mathematics)*100/500
if percentage>=90:
	print("grade a",percentage)
elif percentage>=80:
	print("grade b",percentage)
elif percentage>=70:
	print("grade c",percentage)
elif percentage>=60:
	print("grade d",percentage)
elif percentage>=50:
	print("grade e",percentage)
else:
	print("fail")