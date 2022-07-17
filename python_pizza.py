#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")



#size pricing
cost = 0

if size == "S":
    cost += 15
elif size == "M":
    cost += 20
else:
    cost += 25

#add pep
if add_pepperoni == "Y" and size == "S":
    cost += 2

if add_pepperoni == "Y" and (size == "M" or size == "L"):
    cost += 3

# add cheese
if extra_cheese == "Y":
    cost += 1

print(f"Your final bill is: ${cost}.")




