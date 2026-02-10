# Functions with parameters
# Parameters: they are values that get passed as arguments given to a function inside of the parenthesis


def greeting(name):
    print(f"{name} How are you? hope everything is fine.")

greeting("Natasha")
greeting("Mary")
greeting("Joseph")

print("===================")
def message(names):
    print(f"Hello {names}. We shall be having a general meeting on date.....please avail yourself.")

message("Joy")
message("Steven")

print("===================")
# create a function that accepts parameters to add two numbers
def addition(x, y):
    sum= x + y
    print(f"The sum of the numbers is: {sum}")

addition(46, 37)