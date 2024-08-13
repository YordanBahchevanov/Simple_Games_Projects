from django.db import models


class GameScore(models.Model):
    player_wins = models.IntegerField(default=0)
    ai_wins = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Player: {self.player_wins}, Ai: {self.ai_wins}"
