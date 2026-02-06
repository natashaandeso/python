# Dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use of curly braces {}
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionart we use the keys


phonebook = {
    "Benson" : "2547489309",
    "Mary" : "25471234567",
    "Stephene" : "2547865490"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# printing out benson's number
print(phonebook["Benson"])

print('======================')

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "Phone" : (254704055132, 78905632, 254790563)
    }
}
# print barcelona - the second team he played for
print(player["teams"][1])

# print messi second number
print("The second number of Messi is: ", player["more"][""])

# resaerch on if....else statements in python
# if - do some code only if some condition is true
# Else do something else
# examlpe
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You havent been born yet!")
else:
    print("You must be 18+ to sign up")
# Example two
name = input("Enter your name")

if name == "":
    print("You have not entered your name!")

else:
    print(f"Hello{name}")
    