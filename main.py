import random

def Card():
  cardsDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4
  # Note: there is 4 suits with 13 cards in each suit. 
  #Options = {}
  random.shuffle(cardsDeck)
  pCards = []
  dCards = []
  while len(pCards) != 2:
    pCards.append(cardsDeck.pop())
    if len(pCards) == 2:
      pSum = sum(pCards)
      print("Player has "+str(pSum))
  while pSum <= 21:
    choices = int(input("Would you like to draw more (1) or hold onto your deck (2)? "))
    if (choices == 1):
      pCards.append(cardsDeck.pop())
      pSum = sum(pCards)
      print("Player has "+str(pSum))
      if (pSum > 21):
        print("Player loses.")
        break
      elif (pSum == 21):
        print("Player wins")
        break

def Setup():
  print("Welcome to 21/Blackjack")
  print(""" What would you like?
            -P Vs. P 
            -P Vs. AI """)
  Dict = {"1":PvP()}
  while True:
    try:
      Dict[gamemode()]
      break
    except Keyerror:
      continue