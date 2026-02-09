# A program  to store some gross salary in a variable.
income = int(input("Enter Gross Income in Kshs :"))
# contribution = float(input("Monthly contribution in Kshs"))

if income > 0 and income < 5999:
        print("Your monthly contribution is : 150.00")
elif income >= 6000 and income <= 7999:
        print("Your monthly contribution is : 300.00")
elif income >=8000 and income <=1199:
        print("Monthly contribution is : 400.00")
elif income >=12000 and income <=14999:
        print("Monthly contribution is : 500.00")
elif income >=15000 and income <=19999:
        print("Monthly contribution is : 600.00")
elif income >=20000 and income <=24999:
        print("Monthly contribution is : 750.00")
elif income >=25000 and income <=29999:
        print("Monthly contribution is : 850.00")
elif income >=30000 and income <=49999:
        print("Monthly contribution is : 1000.00")
elif income >=50000 and income <=99999:
        print("Monthly contribution is : 1500.00")
elif income >100000:
        print("Monthly contribution is : 2000.00")
else:
        print("Monthly contribution is : 2000.00")
