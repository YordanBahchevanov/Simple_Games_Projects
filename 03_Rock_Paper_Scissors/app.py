import random
import sys


class RPS:
    PLAYER_WINS = 0
    AI_WINS = 0

    def __init__(self):
        print("Welcome to RPS!")

        self.moves: dict = {"rock": "🤘", "paper": "📜", "scissors": "✂"}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input("Rock, paper, or scissors? >> ").lower()

        if user_move == "exit":
            print("Thanks for playing!")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move...")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print("----")
        print(f"You: {self.moves[user_move]}")
        print(f"You: {self.moves[ai_move]}")
        print("----")

    @staticmethod
    def check_moves(user_move: str, ai_move: str):
        if user_move == ai_move:
            print("It's a tie!")
        elif (user_move == "rock" and ai_move == "scissors") or \
                (user_move == "scissors" and ai_move == "paper") or \
                (user_move == "paper" and ai_move == "rock"):
            RPS.PLAYER_WINS += 1
            print("You win!")
        else:
            RPS.AI_WINS += 1
            print("AI wins...")

        print(f"Player: {RPS.PLAYER_WINS}")
        print(f"AI: {RPS.AI_WINS}")


if __name__ == "__main__":
    rps = RPS()

    while True:
        rps.play_game()
