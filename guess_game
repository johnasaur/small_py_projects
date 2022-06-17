# import relevant files
from art import logo, vs
from game_data import data
import random
from replit import clear

#choose a random name
def random_choice():
  return random.choice(data)

#format choices
def format_choices(data_game):
  name = data_game["name"]
  description = data_game["description"]
  country = data_game["country"]
  return (f"{name}, {description} from {country}")

#once format is done, compare accounts
def compare_accounts(pick, compare_a, compare_b):
  if compare_a > compare_b:
    return pick == "a"
  else:
    return pick == "b"

def game():
  score = 0
  compare_a_acc = random_choice()
  compare_b_acc = random_choice()
  game_continues = True

  while game_continues:
    compare_a_acc = compare_b_acc
    compare_b_acc = random_choice() 

    while compare_a_acc == compare_b_acc:
      compare_b_acc = random_choice()

      print(f"compare A: {format_choices(compare_a_acc)}")
      print(f"compare B: {format_choices(compare_b_acc)}")

      # guess input
      pick = input("Who has more followers? A or B? ").lower()
      pick_count_a = compare_a_acc["follower_count"]
      pick_count_b = compare_b_acc["follower_count"]
      its_correct = compare_accounts(pick, pick_count_a, pick_count_b)
      clear()

      if its_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
      else:
        game_continues = False
        print(f"Sorry, that's wrong. Final score: {score}")

game()
