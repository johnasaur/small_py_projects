# guess a number based on easy or hard level

from random import randint

easy_guesses = 10
hard_guesses = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("too high")
    return turns - 1
  elif guess < answer:
    print("too low")
    return turns -1
  else:
    print(f"you're right, the answer is {answer}")

def set_difficulty():
  hard_or_easy = input("Choose hard or easy: ")
  if hard_or_easy == 'easy':
    return easy_guesses
  else:
    return hard_guesses

def game():
  print("Pick a number btw 1 and 100: ")
  answer = randint(1,100)
  turns = set_difficulty()
  guess = 0

  while guess != answer:
    print(f"you have {turns} attempts left")
    guess = int(input("guess again: "))

    # take 1 guess away each time if wrong number is guessed
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print(f"You've run out of guesses, you lose. the answer is {answer}")
      return
    elif guess != answer:
      print("guess again")
      
game()






