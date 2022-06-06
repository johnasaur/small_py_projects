#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
lower_case = combined_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
total_t = t + r+ u+ e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
total_l = l+o+v+e

score_total = str(total_t) + str(total_l)
int_score = int(score_total)
#print(score_total)

if int_score < 10 or int_score > 90:
    print(f"Your score is {int_score}, you go together like coke and mentos.")
elif int_score in range(40,50):
    print(f"Your score is {int_score}, you are alright together.")
else:
    print(f"Your score is {int_score}.") 




