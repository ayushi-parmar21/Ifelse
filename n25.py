held=int(input("enter held attendence: "))
attendence=int(input("enter attendence: "))
persentage=(attendence/held)*100
if persentage>=75:
    print("allowed to sit in the exam: ")
else:
    print("sorry you are not allowed to the exam becauce your attendece are very less:")