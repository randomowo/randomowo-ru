from django.db import models


class Wish(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    username = models.CharField(max_length=100)
    film_url = models.URLField(null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlist"

    def __str__(self):
        return "{} by [{}]".format(self.name, self.username)
