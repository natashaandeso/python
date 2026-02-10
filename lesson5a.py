# Python functions
# They are a block of code /statements that performs a given task/action. They can be reused throughout the program to perform different tasks.
# Functions are defined using the def keyword. (define)
# We have two main types of functions i.e:
# 1. In-biult function -> They come preinstalled with the interpreter i.e print(), pop(), range(), append() e.t.c
# 2. User defined functions => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the function body it is usualy intented and to invoke a function we use the function name.


def greetings():
    print("Hello, how are you?")

# below we call the function by use of its name
greetings()

print('================================')
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

addition()

print('================================')
# create a function that is able to multiply three values
def multiplication():
    num1 = 2
    num2 = 4
    num3 = 5
    product=num1 * num2 * num3
    print("The product of the numbers is: ", product)

multiplication()

print('================================')
# Below is a division function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The answer is: ", quotient)
    print('--------')


for functio in range(3):
    divide()