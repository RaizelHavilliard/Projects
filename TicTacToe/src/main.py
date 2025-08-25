import random

class TicTacToe:
    def __init__(self):
        self.board = ['  '] * 10
        self.player_turn = self.get_random_first_player()
    def get_random_first_player(self):
        return 'X' if random.randint(0,1) == 0 else 'O'    

    def fix_choice(self, cell, player):
        self.board[cell] = player
        
    def has_player_won(self, player):
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), 
                            (3, 6, 9), (2, 5, 8), (1, 4, 7),
                            (1, 5, 9), (3, 5, 7)]
        for combinations in win_combinations:
            if self.board[combinations[0]] == self.board[combinations[1]] == self.board[combinations[2]] == player:
                return True
        return False

    def change_turn(self):
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        


    def show_board(self):
        print('\n', self.board[1], '|', self.board[2], '|', self.board[3], '\n', '_' * 12)
        print('\n', self.board[4], '|', self.board[5], '|', self.board[6], '\n', '_' * 12)
        print('\n', self.board[7], '|', self.board[8], '|', self.board[9])

    
    def reset_board():
        self.board = ['  '] * 10
        self.player_turn = self.get_random_first_player()

game = TicTacToe()    



def start():
    while True:
        game.show_board()
        print(f'player, {game.player_turn} it\'s your turn')
        
        cell = int(input('which one is your choosen cell?: '))

        if game.board[cell] == '  ':
            game.fix_choice(cell, game.player_turn)   
        else:
            print('cell is already taken, try again')
            continue


        if game.has_player_won(game.player_turn):
            print('congrats, you won')
            hola = input('you wanna play again?: [y/n]')
            if hola.lower() == 'y':
                game.reset_board()
            else:
                break

        if '  ' not in game.board[1:]:
           game.show_board()
           print("It's a draw!")
           break
        else:
            game.change_turn()
            print(f'player, {game.player_turn}, it\'s your turn') 


start()