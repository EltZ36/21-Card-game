#goals: -finish game -make code cleaner -make it OOP if possible 
import random

cardsDeck = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4
cardsDeck2 = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]*4
bet = 0 
dCards = [] 
dSum = sum(dCards)

def repeat():
  while True:
    try:
      play_again = input("Would you like to play again? (Y) or (N)")
      options = {'Y':Setup, 'y':Setup, ' Y':Setup,' y':Setup, 
      'n':exit, ' n':exit, 'N':exit, ' N':exit}
      print(options[play_again]())
      break
    except KeyError:
      print("Please try to type in y or n.")
      continue
    else:
      break

def DealerMove():
  global dCards
  global dSum
  print("What will the dealer do now?")
  dealerChoice = input("Will the dealer draw (1) or stand? (2)")
  if(dealerChoice == 1):
    dCards.append(cardsDeck.pop())
    dSum = sum(dCards)
  else:
    print("Player goes.")

def P_vs_P():
  #Ace can either be an 11 or 1. I don't know how to do it just yet. 
  global cardsDeck
  global bet
  random.shuffle(cardsDeck)
  pCards = []
  dCards = []
  #Dealer shows cards and have to hit until greater than 16 and should stay if it either 16 or over 16. 
  betquestion = int(input("How much do you want to bet?"))
  print("The player bets"+str(betquestion))
  bet = betquestion
  while len(dCards) != 2:
    dCards.append(cardsDeck.pop())
    dSum = sum(dCards)
    if (len(dCards) == 2):
      print(f"The dealer has {dSum} and the first card of the dealer is {dCards[0]}.")
  while len(pCards) != 2:
    pCards.append(cardsDeck.pop())
    pSum = sum(pCards)
    if (len(pCards) == 2):
      print("Player has "+str(pSum))
      if pSum == 21:
        print("Player wins and gets "+str(bet)+".")
      break
  while pSum < 21:
    choices = int(input("Would you (player) like to draw more (1) or Stand [hold onto your deck (2)]? "))
    if (choices == 1):
      pCards.append(cardsDeck.pop())
      pSum = sum(pCards)
      print("The player now has "+str(pSum)+".")
      if (pSum > 21):
        print("Player loses. The dealer wins!")
        repeat()
      elif (pSum == 21):
        print("Player wins.")
        repeat()
      elif (pSum == 21 and dSum == 21):
        print("It is a tie.")
        repeat()
      else:
        Dealermove()
    elif (choices == 2):
      print("Dealer goes.")
      Dealermove()
      if((pSum > dSum) and (pSum < 21)):
        print("Player wins!")
        repeat()
      else:
        print("Player loses and the dealer gets "+str(bet)+".")
        repeat()
    else:
      print("please enter your choice again.")
      continue

def P_vs_AI():
  global cardsDeck2
  random.shuffle(cardsDeck2)
  pCards = []
  aiCards = []
  betquestion = int(input("How much do you want to bet?"))
  print("The player bets "+str(betquestion))
  bet = betquestion
  while len(aiCards) != 2:
    aiCards.append(cardsDeck.pop())
    aiSum = sum(aiCards)
    if (len(aiCards) == 2):
        print(f"The dealer has {aiSum} and the first card of the dealer is {aiCards[0]}.")
        if aiSum == 21:
          print("Dealer wins and gets "+str(bet)+".")
          repeat()
        print(f"Ai picks {random.choice(aiCards)}")
  while len(pCards) != 2:
    pCards.append(cardsDeck.pop())
    pSum = sum(pCards)
    if (len(pCards) == 2):
      print("Player has "+str(pSum))
      if pSum == 21:
        print("Player wins and gets "+str(bet)+".")
        break
  while pSum < 21:
    choices = int(input("Would you (player) like to draw more (1) or Stand [hold onto your deck (2)]?"))
    if (choices == 1):
      pCards.append(cardsDeck.pop())
      pSum = sum(pCards)
      print("Player has "+str(pSum))
      if (pSum > 21):
        print("Player loses. The dealer wins!")
        repeat()
      elif (pSum == 21):
        print("Player wins!")
        repeat()
      elif (pSum == 21 and aiSum == 21):
        print("It is a tie.")
        repeat()
    elif (choices == 2):
      print("Dealer goes.")
      if((pSum > aiSum) and (pSum < 21)):
        print("Player wins.")
        repeat()
      else:
        print("Player loses and the dealer gets "+str(bet)+".")
        repeat()
    else:
      continue

def Setup():
  print("Welcome to 21/Blackjack")
  Dict = {"1":P_vs_P, "2":P_vs_AI}
  while True:
    try:
      gameMode = input(""" What would you like?
      -P Vs. P (1)
      -P Vs. AI (2)""")
      Dict[gameMode]()
      break
    except KeyError:
      print("Please try again and enter 1 or 2.")
      continue
    else:
      break
Setup()
