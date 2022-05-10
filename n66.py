number=int(input("enter any number: "))
if number>=-9 and number<=9:
    print("number is one digited: ")
elif (number>=-99 and number<=-10) or  (number>=10 and number<=99):
    print("number is two digited: ")
elif (number>=-999 and number<=-100) or  (number>=100 and number<=999): 
    print("number is three digited: ")
else:
    print("number is more than three digited")