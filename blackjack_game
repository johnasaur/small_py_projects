######### This Project Blackjack House Rules #########
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  return sum(cards)

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if computer_score == user_score:
    return "draw"
  elif computer_score == 0:
    return "user loses"
  elif user_score == 0:
    return "user wins"
  elif user_score > 21:
    return "user loses"
  elif computer_score > 21:
    return "computer loses"
  else:
    return "player with highest score wins"

def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  game_over = False
    
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"user score: {user_score}, user cards: {user_cards}")
    print(f"computer score: {computer_score}, computer cards: {computer_cards}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if draw_card == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while computer_score != 0  and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(compare(user_score, computer_score))
  
while input("Do you want to play Blackjack? 'y' or 'n': ") == 'y':
  clear()
  play_game()
