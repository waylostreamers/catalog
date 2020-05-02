from django.db import models


class Genre(models.Model):
    """
    A genre for a piece of music or album.
    """

    JAZZ = "JAZZ"
    ROCK = "ROCK"
    BAROQUE = "BAROQUE"

    CHOICES = [
        (JAZZ, "Jazz"),
        (ROCK, "Rock"),
        (BAROQUE, "Baroque"),
    ]

    description = models.CharField(max_length=256, choices=CHOICES)
