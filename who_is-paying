# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill:

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#get all items
items = len(names)

#dynamic list since it's not definite how many ppl are in the list
choices = random.randint(0, items-1)

#who is paying
paying = names[choices]
print(f"{paying} is paying for the meal")
