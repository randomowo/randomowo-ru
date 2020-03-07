from django.db import models
from filmlist.models import Film


class Challenge(models.Model):
    films = models.ManyToManyField(
        Film,
        related_name="challenges",
        verbose_name="Films",
    )
    task = models.CharField(
        max_length=200,
        verbose_name="Task",
    )
    is_done = models.BooleanField(
        default=False,
        verbose_name="Is done?",
    )

    class Meta:
        ordering = ["task"]
        verbose_name = "Challenges"
        verbose_name_plural = "Challenges"

    def __str__(self):
        return self.task
