user=input("enter your strong password: ")
if len(user)>=6 and len(user)<=16:
    if ("A" in user or "Z" in user) or ("a" in user or "z" in user):
        if "2" in user or "1"in user or "3" in user or "4"in user or "5" in user or "6"in user or "7" in user or "8"in user or "9" in user or "0"in user :
            if "@" in user or "$" in user or "&" in user:
                print("strong password: ")
            else:
                print("special character: ")
        else:
            print("also added number: ")
    else:
        print("upper and lower case both we want: ")
else:
    print("week password: ")