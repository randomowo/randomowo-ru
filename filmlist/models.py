"""
"""
import datetime

import challenges as ch
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


class Actor(models.Model):
    """
    """

    name = models.CharField(
        max_length=100,
        unique=True,
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
        unique=True,
        verbose_name="Director name",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Director"
        verbose_name_plural = "Director"

    def __str__(self):
        return self.name


class Series(models.Model):
    """
    """

    film = models.OneToOneField(
        "Film",
        on_delete=models.CASCADE,
        related_name="series",
        verbose_name="Film",
    )

    episodes = models.IntegerField(verbose_name="Total episodes", )

    class Meta:
        ordering = ["film"]
        verbose_name = "Series"
        verbose_name_plural = "Series"

    def __str__(self):
        return "{} with {} ep".format(self.film.title, self.episodes)


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
        null=True,
        blank=True,
        related_name="film",
        verbose_name="Actor",
    )
    film_url = models.URLField(verbose_name="Url to film page", )
    rating = models.FloatField(
        validators=[MinValueValidator(0.01),
                    MaxValueValidator(10.0)],
        blank=True,
        null=True,
    )
    is_watched = models.BooleanField(default=False, verbose_name="Is watched?")
    is_movie = models.BooleanField(
        default=True,
        verbose_name="Is movie?",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Film"
        verbose_name_plural = "Film"

    def __str__(self):
        return "{} ({})".format(self.title, self.year)

    @property
    def is_challenge(self):
        """
        """
        return (True if ch.models.FilmChallenge.objects.filter(
            film=self).first() else False)

    @property
    def episodes(self):
        """
        """
        return Series.objects.get(film__id=self.id).episodes

    @property
    def info(self):
        """
        """
        if self.is_movie:
            return "in [{}] by {} [{}]".format(self.year, self.director.name,
                                               "x" if self.is_watched else " ")
        else:
            return "with {} ep in [{}] by {} [{}]".format(
                self.episodes,
                self.year,
                self.director.name,
                "x" if self.is_watched else " ",
            )
