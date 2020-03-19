"""
"""
from django.db import models
from filmlist.models import Film


class FilmChallenge(models.Model):
    """
    """
    film = models.OneToOneField(
        Film,
        on_delete=models.CASCADE,
        related_name="challenges",
        verbose_name="Film",
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Is done?",
    )

    class Meta:
        ordering = ["film"]
        verbose_name = "Challenged film"
        verbose_name_plural = "Challenged film"

    def __str__(self):
        return "{} [{}]".format(self.film.title, "x" if self.is_done else " ")


class Challenge(models.Model):
    """
    """
    films = models.ManyToManyField(
        FilmChallenge,
        related_name="challenges",
        verbose_name="Challenge",
    )
    task = models.CharField(
        max_length=200,
        verbose_name="Task",
    )

    class Meta:
        ordering = ["task"]
        verbose_name = "Challenge"
        verbose_name_plural = "Challenge"

    def __str__(self):
        return self.task
