def exitting():
  if input("Do you wanna play again? ").lower()=="no":
    return False
  else:  
    return True
from random import choice
from replit import clear
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
to_play=True
while to_play: 
  clear()
  usercards=[choice(cards),choice(cards)]
  compcards=[choice(cards),choice(cards)]
  userscore=sum(usercards)
  compscore=sum(compcards)
  print(f"Your cards: {usercards}. Current score = {userscore}")
  print(f"Computer's 1st card: {compcards[0]}.")
  if userscore>21 and compscore<=21:
    print("Your score exceeded 21. You Lose.")
    print(f"Computer's deck: {compcards}. Computer's score: {compscore}")
    to_play=exitting()
    continue
  elif compscore>21 and userscore<=21:
    print(f"Computer's score exceeds 21. You win!\nComputer's deck: {compcards}. Computer's score: {compscore}.")
    to_play=exitting()
    continue
  elif compscore>21 and userscore>21:
    print(f"Both computer's score and you score exceeds 21. It's a tie :(\nComputer's deck: {compcards}. Computer's score: {compscore}.")
    to_play=exitting()
    continue
  if userscore==21 and compscore==21:
    print(f"Both computer's score and you score is 21. It's a tie :(\nComputer's deck: {compcards}. Computer's score: {compscore}.")
    to_play=exitting()
    continue
  elif userscore==21:
    print(f"You got a BLACKJACK. You win!\nComputer's deck: {compcards}. Computer's score: {compscore}.")
    to_play=exitting()
    continue
  elif compscore==21:
    print(f"Computer got a BLACKJACK. You lose!\nComputer's deck: {compcards}. Computer's score: {compscore}.")
    to_play=exitting()
    continue
  userdraw=True
  while userdraw:
    if userscore>=21:
      userdraw=False
    else:
      drawcard=input("Do you wish to draw another card? 'y' or 'n': ")
      if drawcard=='y':
        usercards.append(choice(cards))
        userscore=sum(usercards)
        print(f"Your cards: {usercards}. Current score = {userscore}")
      else:
        userdraw=False
  if userscore>21:
    print("Your score exceeded 21. You Lose.")
    print(f"Computer's deck: {compcards}. Computer's score: {compscore}")
    to_play=exitting()
  else:
    while compscore<17:
      compcards.append(choice(cards))
      compscore=sum(compcards)
    if compscore>21:
      print(f"Computer's score exceeds 21. You win!\nComputer's deck: {compcards}. Computer's score: {compscore}.")
      to_play=exitting()
      continue
    elif compscore==userscore:
      print(f"Both computer's score and you score is {compscore}. It's a tie :(\nComputer's deck: {compcards}. Computer's score: {compscore}.")
      to_play=exitting()
      continue
    elif userscore>compscore:
      print(f"Your score {userscore} is greater than computer's score {compscore}. You win!\nComputer's deck: {compcards}. Computer's score: {compscore}.")
      to_play=exitting()
      continue
    elif compscore>userscore:
      print(f"Your score {userscore} is lower than computer's score {compscore}. You lose!\nComputer's deck: {compcards}. Computer's score: {compscore}.")
      to_play=exitting()
      continue
      
    
      
      
    
  
    
    
    
        
    

    
 
    
  

  
