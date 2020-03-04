from django.db import models


class Challenge(models.Model):
    task = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="Challenge?")

    class Meta:
        ordering = ["task"]
        verbose_name = "Challenges"
        verbose_name_plural = "Challenges"

    def __str__(self):
        return self.task
