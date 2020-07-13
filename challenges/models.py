"""
"""
import math

from django.core.validators import MinValueValidator
from django.db import models

from filmlist.models import Film


class FilmChallenge(models.Model):
    """
    """

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name="challenges",
        verbose_name="Film",
    )

    challenge = models.ForeignKey(
        "Challenge",
        on_delete=models.CASCADE,
        related_name="filmchallenge",
        verbose_name="Challenge",
        null=True,
    )

    is_done = models.BooleanField(
        default=False,
        verbose_name="Is done?",
    )

    position = models.IntegerField(
        default=1,
        verbose_name="Position",
        validators=[MinValueValidator(1)],
    )

    class Meta:
        ordering = ["position"]
        verbose_name = "Challenged film"
        verbose_name_plural = "Challenged film"

    def __str__(self):
        return "{} [{}]".format(self.film.title, "x" if self.is_done else " ")


class Challenge(models.Model):
    """
    """

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

    @property
    def progress(self):
        chlist = [
            ch.is_done
            for ch in FilmChallenge.objects.filter(challenge=self).all()
        ]
        return 0 if not chlist else int(math.floor(100 * (chlist.count(True) / len(chlist))))
