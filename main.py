#goals: -finish game -make code cleaner -make it OOP if possible 
import random

cardsDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4
cardsDeck2 = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4

def repeat():
  while True:
    try:
      play_again = input("Would you like to play again? (Y) or (N)")
      options = {'Y':PvP, 'y':PvP, ' Y':PvP,' y':PvP, 
      'n':exit, ' n':exit, 'N':exit, ' N':exit}
      print(options[play_again]())
      break
    except KeyError:
      print("Please try to type in y or n")
      continue
    else:
      break
      
def PvP():
  #Ace can either be an 11 or 1. I don't know how to do it just yet. 
  global cardsDeck
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
      print(f"The dealer has {dSum} and the first card of the dealer is {dCards[0]}")
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
        repeat()
      elif (pSum == 21):
        print("Player wins")
        repeat()
      elif (pSum == 21 and dSum == 21):
        print("It is a tie.")
        repeat()
    elif (choices == 2):
      print("Dealer goes.")
      if((pSum > dSum) and (pSum < 21)):
        print("Player wins")
        repeat()
      else:
        print("Player loses")
        repear()
      DealerMove()
    else:
      break

def PvAI():
  global cardsDeck2
  random.shuffle(cardsDeck2)
  pCards = []
  aiCards = []
  while len(aiCards) != 2:
    aiCards.append(cardsDeck.pop())
    aiSum = sum(aiCards)
    if (len(aiCards) == 2:
        return None
    #Add random here 

def DealerMove():
  print("What will the dealer do now?")
  print("Will the dealer stand (1) or hit (2)")
  while True:
        try:
          return 
        except TypeError:
          print("Please try again.")

def Setup():
  print("Welcome to 21/Blackjack")
  Dict = {"1":PvP, "2":PvAI}
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
