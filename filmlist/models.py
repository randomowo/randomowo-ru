import datetime

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class Actor(models.Model):
    """
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Actor name",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Actor"
        verbose_name_plural = "Actor"

    def __str__(self):
        return self.name


class Director(models.Model):
    """
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Director name",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Director"
        verbose_name_plural = "Director"

    def __str__(self):
        return self.name


class Film(models.Model):
    """
    """

    title = models.CharField(max_length=100, )
    year = models.IntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(datetime.date.today().year + 1),
    ])
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name="film",
        verbose_name="director",
    )
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
        related_name="film",
        verbose_name="Actor",
    )
    is_watched = models.BooleanField(default=False, verbose_name="Is watched?")
    rating = models.FloatField(
        validators=[MinValueValidator(0.01),
                    MaxValueValidator(10.0)],
        blank=True,
        null=True,
    )
    is_movie = models.BooleanField(
        default=False,
        verbose_name="Is movie?",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Film list"
        verbose_name_plural = "Film list"

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


class Series(models.Model):
    """
    """

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name="series",
        verbose_name="Film",
    )

    episodes = models.IntegerField(verbose_name="Total episodes", )

    class Meta:
        ordering = ["film"]
        verbose_name = "Series"
        verbose_name_plural = "Series"
