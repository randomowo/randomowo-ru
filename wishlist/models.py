from django.db import models


class Wish(models.Model):
    title = models.CharField(max_length=100, db_index=True, unique=True)
    username = models.CharField(max_length=100)
    film_url = models.URLField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlist"

    def __str__(self):
        return "{} by user {}".format(self.title, self.username)
