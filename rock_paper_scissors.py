#Make a rock, paper, scissors game:

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps_list = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

#my input
#00: draw
#01: paper covers rock, comp wins
#02: rock crushes scissors, you win
#10: paper covers rock, you win
#11: draw
#12: scissors cut paper, comp wins
#20: rock crushes scissors, comp wins
#21: scissors cut paper, you win
#22: draw


import random
#rps_list =[0,1,2]
comp_list = random.randint(0,2)
if rps_list == 0 and comp_list == 0:
  print("It's a draw, try again.")
elif rps_list == 0 and comp_list == 1:
  print("paper covers rock, comp wins")
elif rps_list == 0 and comp_list == 2:
  print("rock crushes scissors, you win")
elif rps_list == 1 and comp_list == 0:
  print("paper covers rock, you win")
elif rps_list == 1 and comp_list == 1:
  print("It's a draw, try again.")
elif rps_list == 1 and comp_list == 2:
  print("scissors cut paper, comp wins")
elif rps_list == 2 and comp_list == 0:
  print("rock crushes scissors, comp wins")
elif rps_list == 2 and comp_list == 1:
  print("scissors cut paper, you win")
elif rps_list == 2 and comp_list == 2:
  print("It's a draw, try again.")
else:
  print("error, try again")
  

