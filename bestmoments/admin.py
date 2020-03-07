from django.contrib import admin
from bestmoments.models import BestImage

class BestImageAdmin(admin.ModelAdmin):
    """
    """
    list_display = ["image"]

admin.site.register(BestImage, BestImageAdmin)
