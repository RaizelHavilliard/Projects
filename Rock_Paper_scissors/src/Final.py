import random

class RockPaperScissors:
    """
    A class to represent a Rock, Paper, or Scissor choice.

    Attributes:
        name (str): The name of the choice (Rock, Paper, Scissor).
    """

    def __init__(self, name):
        """
        Initialize the RockPaperScissors object.

        Args:
            name (str): The name of the choice.
        """
        self.name = name

    def __repr__(self):
        """
        Return a string representation of the object.

        Returns:
            str: The name of the choice.
        """
        return f"{self.name}"
    

# Define the available choices
C1 = RockPaperScissors("Rock")
C2 = RockPaperScissors("Paper")
C3 = RockPaperScissors("Scissor")

Items = [C1, C2, C3]


def get_Computer_choice():
    """
    Randomly select one choice for the computer.

    Returns:
        RockPaperScissors: The computer's random choice.
    """
    return random.choice(Items)


def get_player_choice():
    """
    Ask the player for their choice and validate it.

    Returns:
        str: The player's valid choice (rock, paper, scissor).
    """
    player_choice = input("Please type your choice between; Rock, Paper, Scissor: ")
    if player_choice.lower() not in ["rock", "paper", "scissor"]:
        print("Invalid answer, try again.")
        return get_player_choice()
    return player_choice


def compare(player_choice, computer_choice):
    """
    Compare player's choice with computer's choice to determine the winner.

    Args:
        player_choice (str): The choice made by the player.
        computer_choice (RockPaperScissors): The choice made by the computer.

    Returns:
        str: The result of the game (tie, player win, or computer win).
    """
    if player_choice == computer_choice.name:
        return "It's a tie!"
    elif (player_choice == "paper" and computer_choice.name == "Rock") or \
         (player_choice == "rock" and computer_choice.name == "Scissor") or \
         (player_choice == "scissor" and computer_choice.name == "Paper"):
        return "Woah!! You won"
    else:
        return "Oops, computer won"


def play():
    """
    Play one round of Rock, Paper, Scissors.

    Gets the player's choice, generates the computer's choice,
    compares them, and prints the result.
    """
    player_choice = get_player_choice()
    computer_choice = get_Computer_choice()
    print("Computer choice:", computer_choice)
    result = compare(player_choice.lower(), computer_choice)
    print(result)


# Main game loop
while True:
    play()
    continue_game = input("Do you want to play again? [y/n]: ")
    if continue_game.lower() == "n":
        break
