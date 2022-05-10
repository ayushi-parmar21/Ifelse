unit=int(input("enter no of unit you consumed"))
if unit<=50:
      charge=unit*0.50+unit*20/100
elif unit>50 and unit<=100:
     charge=50*0.50+(unit-50)*0.75+unit*20/10
elif unit>100 and unit<=250:
     charge=50*0.50+100*0.75+(unit-150)*1.20+unit*20/100
else :
      charge=unit*1.50+unit*20/100
print("total charge:",charge)