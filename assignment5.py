def area():
    num1 = 4
    num2 = 5
    area=num1 * num2 
    print("The area of a triangle is: ", area)

area()

print("==============================")
def my_function(x, y):
    sum = x + y
    difference = x - y
    product = x * y
    quantine = x / y
    print(f"The sum of the numbers is: {sum}")
    print(f"The difference of the numbers is: {difference}")
    print(f"The product of the numbers is: {product}")
    print(f"The quantine of the numbers is: {quantine}")

my_function(6, 24)

print("==============================")

number = int(input("Enter number: "))

if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")


print("==============================")

def sum_of_numbers(n):
    sum= 0
    for i in range(1, n+1):
         sum+=i
    print("The sum of numbers from 1 to",n,"is:",sum)
n=int(input("Enter a number: "))
sum_of_numbers(n)
print('=============================')


def square_of_numbers(n):
    i=1
    while i<=n:
        square=i**2
        print("The square of",i,"is:",square) 
        i+=1
n=int(input("Enter a number: "))
square_of_numbers()
