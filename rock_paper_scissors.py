import random 

print("||-> Logic : Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. <-||")

while True :

  def game(comp, you): 
    if comp == you :
      print("Game Tie!")
    else :
      if comp == "r" :
        if you == "p" :
          print("You win the game")
        elif you == "s" :
          print("You lose the game")
      elif comp == "p" :
        if you == "s" :
          print("You win the game")
        elif you == "r" :
          print("You lose the game")
      elif comp == "s" :
        if you == "r" :
          print("You win the game")
        elif you == "p" :
          print("You lose the game")
  ranNO = random.randint(1, 3)

  print("Enter your choice")
  you = input("for Rock(r), for Paper(p) for Scissors(s) : ")

  if ranNO == 1 :
    comp = "r"
  elif ranNO == 2 :
    comp = "p"
  elif ranNO == 3:
    comp = "s"

  print(f"computer choice is : {comp}")
  print(f"Your choice is : {you}")

  print("")
  print("---------------------")
  Gwin = game(comp, you)
  print("---------------------")
  print("")

  ask = input("Play again? (YES/NO) : ")
  print("")
  if ask.lower() != "yes" :
    break