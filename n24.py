first=int(input("enter first persone age: "))
second =int(input("enter second persone age: "))
third=int(input("enter third persone age: "))

if first>=second and first>=third and second>=third:
    print("oldest is first: ",first)
    print("youngest is third: ",third)
elif first>=second and first>=third and second<=third:
    print("oldest is first: ",first)
    print("youngest is third: ",second)
elif second>=first and second>=third and first>=third:
    print("oldest is secomd: ",second)
    print("youngest is third: ",third)
elif second>=first and second>=third and first<=third:
    print("oldest is second: ",second)
    print("youngest is first: ",first)
elif third>=second and third>=first and first>=second:
    print("oldest is third: ",third)
    print("youngest is second: ",second)
elif third>=second and third>=first and first<=second:
    print("oldest is third: ",third)
    print("youngest is first: ",first)
else:
    print("all are equa: ")