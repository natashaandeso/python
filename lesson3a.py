# Boolean - This is a data type that evaluates either true or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidLoan = True
print(paidLoan)
print(type(paidLoan))

# comparison operators: They are used to compare two or more statements and they ussualy return a boolean answer

number1 = 2
number2 = 5

print("is number1 greater than number2? ", number1 > number2)
print("is number1 less than number2? ", number1 < number2)
print("is number1 greater than or equal to number2? ", number1 >= number2)
print("is number1 less than or equal to number2? ", number1 <= number2)
print("is number1 equal to number2? ", number1 == number2)
print("is number1 not equal to number2? ", number1 != number2)

# Logical operators
# Logical AND
# It returns true if and only if the condition/statements evaluates to true
print((3 > 1) and (7 > 6))

# Logical or
# It evaluates to true if one of the statements/condition is true
print((3 > 1) or (7 < 6))

# Logical not
# It is used to negate a statement/condition
print(not(90 > 70))