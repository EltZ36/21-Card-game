#goals: -finish game -make code cleaner -make it OOP if possible 
import random

def PvP():
  #Ace can either be an 11 or 1. I don't know have to do it
  cardsDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4
  # Note: there is 4 suits with 13 cards in each suit. 
  #Options = {}
  random.shuffle(cardsDeck)
  pCards = []
  dCards = []
  #Dealer shows cards and have to hit until greater than 16 and should stay if it either 16 or over 16. 
  while len(dCards) != 2:
    dCards.append(cardsDeck.pop())
    dSum = sum(dCards)
    if (len(dCards) == 2):
      print("The dealer has "+str(dSum)+" and the first card of the dealer is "+str(dCards[0]))
  while len(pCards) != 2:
    pCards.append(cardsDeck.pop())
    pSum = sum(pCards)
    if (len(pCards) == 2):
      print("Player has "+str(pSum))
      break
    if pSum == 21:
      print("Player has "+str(pSum))
      print("Player wins")
      break
  while pSum < 21:
    choices = int(input("Would you (player) like to draw more (1) or Stand [hold onto your deck (2)]? "))
    if (choices == 1):
      pCards.append(cardsDeck.pop())
      pSum = sum(pCards)
      print("Player has "+str(pSum))
      if (pSum > 21):
        print("Player loses. The dealer wins!")
        break
      elif (pSum == 21):
        print("Player wins")
        break
    else:
      break
      
def Setup():
  print("Welcome to 21/Blackjack")
  Dict = {'1':PvP, '2':None}
  while True:
    try:
      gameMode = input(""" What would you like?
      -P Vs. P (1)
      -P Vs. AI (2)""")
      Dict[gameMode]()
      break
    except KeyError:
      print("Please try again and enter 1 or 2")
      continue
    else:
      break
Setup()
