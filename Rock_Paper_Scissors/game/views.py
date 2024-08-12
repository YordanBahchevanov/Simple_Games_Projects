from django.shortcuts import render
import random


def index(request):
    moves = {"rock": "🤘", "paper": "📜", "scissors": "✂"}
    valid_moves = list(moves.keys())

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
        return render(request, 'game/templates/index.html', context)

    return render(request, 'game/templates/index.html')


def check_moves(user_move, ai_move):
    if user_move == ai_move:
        return "It's a tie!"
    elif (user_move == "rock" and ai_move == "scissors") or \
            (user_move == "scissors" and ai_move == "paper") or \
            (user_move == "paper" and ai_move == "rock"):
        return "You win!"
    else:
        return "AI wins..."
