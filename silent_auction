#Build a silent auction program

from replit import clear
from art import logo
print(logo) # gavel ASCII art

silent_auction = {}
finished_bidding = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finished_bidding:
  add_name = input(f"Write your name: ")
  add_price = int(input(f"Name your price: $"))
  silent_auction[add_name] = add_price
  other_bidders = input(f"Are there more bidders? yes or no ")
  clear()
  if other_bidders == "no":
    finished_bidding = True
    highest_bidder(silent_auction)




