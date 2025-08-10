import random

def start_game():
    game_num = random.randint(1, 100)
    score = 100

    while True:
        input_num = input("hi please enter your guess: ")
        user_guess = input_num

        if user_guess == "q":
            print("thank you good bye")
            break

        elif not user_guess.isdigit():
            print("invalid value please enter a number between 1 and 100")
            continue

        else: 
            user_guess = int(input_num)
            if user_guess > 100 or user_guess < 0:
                print("keep it in the range of 1 to 100")
                continue
    
    
        user_guess = int(user_guess)
        if user_guess == game_num:
            print(f"congrats!! you guessed correctly your score is {score}")
            wanna_play = input("do you wanna play again?(y/n) ")
            if wanna_play == "y":
                game_num = random.randint(1, 100)
                score == 100 
                continue
            else: 
                print("bye bye")
                break
        elif user_guess > game_num:
            print("too high try again")
        elif user_guess < game_num:
            print("too low try again")

        score -= 5
        score = max(score, 0)
                    
            
if __name__ == '__main__':
    start_game()
    
