from django.shortcuts import render
import random


def index(request):
    moves: dict = {"rock": "🤘", "paper": "📜", "scissors": "✂"}
    valid_moves: list[str] = list(moves.keys())

    if request.method == "POST":
        user_move = request.POST.get("move")
        ai_move = random.choice(valid_moves)

        result = check_moves(user_move, ai_move)
        context = {
            "user_move": user_move,
            "ai_move": ai_move,
            "result": result,
            "player_wins": request.session.get("player_wins", 0),
            "ai_wins": request.session.get("ai_wins", 0),
        }
        return render(request, "templates/index.html", context)

    return render(request, "templates/index.html")


def check_moves(user_move: str, ai_move: str):
    if user_move == ai_move:
        print("It's a tie!")
    elif (user_move == "rock" and ai_move == "scissors") or \
            (user_move == "scissors" and ai_move == "paper") or \
            (user_move == "paper" and ai_move == "rock"):
        print("You win!")
    else:
        print("AI wins...")
