# Create a python program that is able to determine whether a number entered is an odd number or an even number.
# number = int(input("Enter the number"))

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person. If the weight is  greater than 50kg and age is above 18 ,then the person can donate blood
age = int(input("Enter your age: "))

weight = float(input("Enter your weight: "))

if age >= 100:
    print("You are too old to donate blood")
elif age >= 18 and weight > 50:
    print("You can donate blood")

else:
    print("You cannot donate")

# Nested if statements
# Loops in python
