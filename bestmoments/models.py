"""
"""
from django.db import models
from django.conf import settings

class BestImage(models.Model):
    """
    """

    image = models.ImageField(
        upload_to="best_moments/",
        verbose_name="Best moment image",
    )

    class Meta:
        ordering = ["image"]
        verbose_name = "Image"
        verbose_name_plural = "Image"

    def __str__(self):
        return "{}{}".format(settings.MEDIA_URL, self.image)
