import datetime

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


def year_choices():
    return [(r, r) for r in range(1900, datetime.date.today().year + 1)]


class Film(models.Model):
    """
    """
    name = models.CharField(
        max_length=100,
    )
    year = models.IntegerField(choices=year_choices(), )
    autor = models.CharField(
        max_length=100,
        blank=True,
    )
    watched = models.BooleanField(default=False, verbose_name="Watched?")
    rating = models.FloatField(
        validators=[MinValueValidator(0.01),
                    MaxValueValidator(10.0)],
        blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Film list"
        verbose_name_plural = "Film list"

    def __str__(self):
        return "{} ({})".format(self.name, self.year)
