ayushi=input("stone,paper and sizer choice ayushi: ")
nikita=input("stone,paper and sizer choice nikita: ")
if ayushi=="stone" and nikita=="paper":
	print("nikita win")
elif ayushi=="paper" and nikita=="stone":
	print("ayushi win")
elif ayushi=="scissor" and nikita=="paper":
	print("ayushi win")
elif ayushi=="paper" and nikita=="scissor":
	print("nikita win")
elif ayushi=="scissor" and nikita=="stone":
	print("nikita win")
elif ayushi=="stone" and nikita=="scissor":
	print("ayushi win")
else :
	print("both are equal")