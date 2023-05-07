from replit import clear
from art2 import logo
print(logo)

bid_parties = {}
more_bids = False

def highest_bidder(bidding_record):
  high_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amt = bidding_record[bidder]
    if bid_amt > high_bid:
      high_bid = bid_amt
      winner = bidder
  print(f"The winner is {winner} with a bid of ${high_bid}")


print("Welcome to the secret auction program.")


while not more_bids:
  name = input("What is your name?")
  bid_price = input("What is your bid?")
  bid_parties[name] = bid_price
  more_bids = input("Are there any other bidders? Type yes or no.").lower
  if more_bids == "no":
    more_bids = True
    highest_bidder(bid_parties)
  elif more_bids == "yes":
    clear()

