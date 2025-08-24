import random

first_choice = int(input("your choosen door?!:"))
def Monty_hall_doors(switch_doors):

    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)


    door_revealed = [i for i in range(3) if i != first_choice and doors[i] == 'goat']
    door_revealed = random.choice(door_revealed)

    if switch_doors:
        final_choice = [i for i in range(3) if i != door_revealed and i != first_choice][0]
    else:
        final_choice = first_choice

    return doors[final_choice] == 'car'    


def simulating_game():
    num_games = int(input("how many time you wanna simulate?:"))
    num_with_switch = sum(Monty_hall_doors(switch_doors=True) for _ in range(num_games))
    num_without_switch = sum(Monty_hall_doors(switch_doors=False) for _ in range(num_games))
    return num_with_switch, num_without_switch

print(simulating_game())