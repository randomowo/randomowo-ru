"""
"""
from django.db import models
from django.conf import settings
from utilities import compress_image

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

    def save(self, *args, **kwargs):
        """
        """
        new_image = compress_image(self.image)
        self.image = new_image
        super().save(*args, **kwargs)
