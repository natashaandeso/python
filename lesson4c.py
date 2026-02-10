# A for loop can also be used to iterate through a list, tuple, string or even a dictionary..

name = "Natasha"

for letter in name:
    if letter == "s":
       print("this is letter s")
    else:
        print(letter)

print('=================')
# Below is a list of countries
counties = ["Nairobr", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print('=================')
for county in counties:
    if "Narok" in counties:
        print("this county is found")
    
    else:
        print("The county is not found")
        break
print('=================')
# The for loop can also be used to iterate through a dictionary

player = {
    "name": "Mbape",
    "age": 25,
    "team": ["PSG", "Monaco", "France"],
    "nationality": "French"
}

for key in player:
    print(key)
print('=================')
for value in player:
    print(player[value])

print('=================')
# loop through the teams
for team in player["team"]:
    print(team)
    

    
        
    
