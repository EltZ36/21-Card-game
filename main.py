import random

def Card():
  numCards = 52
  # Note: there is 4 suits with 13 cards in each suit. 
  random.shuffle(numCards)
  choices = input("Would you like to draw more (1) or hold onto your deck (2)? ")
  print(choices)

def Setup():
  print("Welcome to 21/Blackjack")
  print(""" What would you like?
            -P Vs. P 
            -P Vs. AI """)
  Dict = {}
  while True:
    try:
      return none
      break
    except Keyerror:
      continue
