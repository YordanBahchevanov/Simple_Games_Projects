from django.shortcuts import render
from Rock_Paper_Scissors.game.models import GameScore
import random


def index(request):
    moves = {"rock": "🤘", "paper": "📜", "scissors": "✂"}
    valid_moves = list(moves.keys())

    if request.method == "POST":
        user_move = request.POST.get("move").lower()
        if user_move not in valid_moves:
            return render(request, 'index.html', {"error": "Invalid move!"})

        ai_move = random.choice(valid_moves)

        score, created = GameScore.objects.get_or_create(id=1)

        if user_move == ai_move:
            result = "It's a tie!"
        elif (user_move == "rock" and ai_move == "scissors") or \
             (user_move == "scissors" and ai_move == "paper") or \
             (user_move == "paper" and ai_move == "rock"):
            score.player_wins += 1
            result = "You win!"
        else:
            score.ai_wins += 1
            result = "AI wins..."

        score.save()

        context = {
            "user_move": user_move,
            "ai_move": ai_move,
            "result": result,
            "player_wins": request.session.get("player_wins", 0),
            "ai_wins": request.session.get("ai_wins", 0),
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')


