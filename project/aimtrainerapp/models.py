from django.db import models

from django.utils import timezone

class Score(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-score']  # Orders scores from highest to lowest

    def __str__(self):
        return f"{self.name} - {self.score} - {self.date.strftime('%Y-%m-%d %H:%M')}"