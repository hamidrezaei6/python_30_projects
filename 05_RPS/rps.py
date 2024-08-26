import random
import sys


class RPS:
    def __init__(self):
        print('Welcome To RPS!')

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input('Rock, paper, or scissors? >> ').lower()

        if user_move == 'exit':
            print('thanks for playing...')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid moves...')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)
        self.display_move(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_move(self, user_move: str, ai_move: str):
        print('=====')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('=====')

    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It is a tie...')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('you win!')
        elif user_move == 'scissors' and ai_move == 'paper':
            print('you win!')
        elif user_move == 'paper' and ai_move == 'rock':
            print('you win!')
        else:
            print('AI win!')


if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
