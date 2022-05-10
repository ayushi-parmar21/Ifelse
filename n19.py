basic=int(input("enter your basic salary"))
if basic<=1000:
    HRA=basic*20/100
    DA=basic*80/100
elif basic<=2000:
    HRA=basic*25/100
    DA=basic*90/100
else:
    HRA=basic*30/100
    DA=basic*95/100
gross_salary=basic+HRA+DA
print("Gross salary : ",gross_salary)