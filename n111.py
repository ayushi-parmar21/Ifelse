user=int(input("enter any number: "))
if user>=0 and user<=9:
    print("one digit: ")
elif user>=10 and user<=99:
    print("two digit: ")
else:
    print("greater then two digit: ")