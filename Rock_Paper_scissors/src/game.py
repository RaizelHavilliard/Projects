import random

class RockPaperScissors:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f"{self.name}")
    
C1 = RockPaperScissors("Rock")
C2 = RockPaperScissors("Paper")
C3 = RockPaperScissors("Scissor")

Items = [C1, C2, C3]

def get_Computer_choice():
    return random.choice(Items)

def get_player_choice():
    player_choice = input("please type your choice between; Rock, Paper, Scissor: ")
    if player_choice.lower() not in ["rock", "paper", "scissor"]:
        print("invalid answer, try again")
        return get_player_choice()
    return player_choice 

def compare(player_choice, computer_choice):
    if player_choice == computer_choice.name:
        print("it's a tie!")
    elif player_choice == ("paper") and computer_choice == ("rock") or \
    player_choice == ("rock") and computer_choice == ("scissor") or \
    player_choice == ("scissor") and computer_choice == ("paper"):
        return "woah!! you won"
    else:
        return "oops, computer won"  


def play():
    player_choice = get_player_choice()
    computer_choice = get_Computer_choice()
    print("computer choice:", computer_choice)
    result = compare(player_choice, computer_choice)
    print(result)


while True:
    play()  
    continue_game = input("Do you wanna play again?[y/n]: ")  
    if continue_game.lower() == "n":
        break


