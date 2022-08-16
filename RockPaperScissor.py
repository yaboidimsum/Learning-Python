import random

def get_choices():
  player_choice = input("Enter a choice (Rock,Paper,Scissor):")
  options = ["Rock","Paper","Scissor"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices

def check_win(player,computer):
  print(f"Your choice is {player}, computer choice is {computer}")
  if player == computer:
    return "Tie! No one's won" 
  
  elif player == "Rock":
    if computer == "Scissor":
      return "Rock smashes scissor! You win!"
    else:
      return "Paper wrapped the rock! You lose."
  
  elif player == "Paper":
    if computer == "Rock":
      return "Paper wrapped the rock! You win!"
    else:
      return "Paper got cut! You lose."
  
  elif player == "Scissor":
    if computer == "Paper":
      return "Paper got cut! You win!"
    else:
      return "Rock smashes scissor! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)