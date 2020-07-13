"""
"""
import datetime

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

import challenges as ch

class Episode(models.Model):
    """
    """

    title = models.CharField(
        max_length=120,
        verbose_name="Episode title",
        blank=True,
        null=True,
    )

    number = models.IntegerField(
        verbose_name="No.",
        validators=[MinValueValidator(1)],
    )

    duration = models.IntegerField(
        verbose_name="Episode duration (minutes)",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )

    season = models.ForeignKey(
        "Season",
        on_delete=models.CASCADE,
        related_name="Episode",
        verbose_name="Season",
    )

    class Meta:
        ordering = ["number"]
        verbose_name = "Episode"
        verbose_name_plural = "Episode"

    def __str__(self):
        return 's{0}e{1}: "{2}"'.format(self.season.number, self.number,
                                        self.title)


class Season(models.Model):
    """
    """

    film = models.ForeignKey(
        "Film",
        on_delete=models.CASCADE,
        related_name="Season",
        verbose_name="Film",
    )

    number = models.IntegerField(
        verbose_name="No.",
        validators=[MinValueValidator(1)],
    )

    class Meta:
        ordering = ["number"]
        verbose_name = "Season"
        verbose_name_plural = "Season"

    def __str__(self):
        return "{0} s No.{1}".format(self.film.title, self.number)

    @property
    def episodes(self):
        """
        """
        return Episode.objects.filter(season=self).count()


class Film(models.Model):
    """
    """

    title = models.CharField(
        max_length=120,
        verbose_name="Title",
    )
    year = models.IntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(datetime.date.today().year + 2),
    ])
    director = models.CharField(
        max_length=50,
        verbose_name="Director",
    )
    url = models.URLField(verbose_name="Url to film page", )
    is_watched = models.BooleanField(default=False, verbose_name="Is watched?")
    is_movie = models.BooleanField(
        default=True,
        verbose_name="Is a movie?",
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
    def seasons(self):
        """
        """
        return Season.objects.filter(film=self).count()

    @property
    def episodes(self):
        """
        """
        seasons_list = Season.objects.filter(film=self).all()
        episodes = [s.episodes for s in seasons_list]
        return sum(episodes)

    @property
    def serial(self):
        """
        """
        serial = {}
        for season in Season.objects.filter(film=self).all():
            serial[str(season.number)] = Episode.objects.filter(season=season).all()
        return serial.items()



    @property
    def info(self):
        """
        """
        if self.is_movie:
            return "in [{}] by {} [{}]".format(self.year, self.director,
                                               "x" if self.is_watched else " ")
        else:
            return "with {} ep in [{}] by {} [{}]".format(
                self.episodes,
                self.year,
                self.director,
                "x" if self.is_watched else " ",
            )
