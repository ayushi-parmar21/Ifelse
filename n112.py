user1=int(input("enter a age of first persone "))
user2=int(input("enter a age of second persone "))
user3=int(input("enter a age of third persone "))
if user1>user2 and user1>user3:
    print("first persone is oldest")
elif user2>user3 and user2>user1:
    print("second persone is oldest")
elif user3>user2 and user3>user1:
    print("third persone is oldest")
if user1<user2 and user1<user3:
    print("first persone is youngest")
elif user2<user1 and user2<user3:
    print("second persone is youngest")
elif user3<user2 and user3<user1:
    print("third persone is youngest")
else:
    print("all are equal: ")