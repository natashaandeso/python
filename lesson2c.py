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
    "teams" : ["PSG", "Barcelona", "Argentina"]
}
# print barcelona - the second team he played for
print(player["teams"][1])


# resaerch on if....else statements in python