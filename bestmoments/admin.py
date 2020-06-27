"""
"""
from django.contrib import admin
from bestmoments.models import BestImage
from bestmoments.models import WebmVideo

class BestImageAdmin(admin.ModelAdmin):
    """
    """
    list_display = ["image"]


class WebmVideoAdmin(admin.ModelAdmin):
    """
    """
    list_display = ["video"]

admin.site.register(BestImage, BestImageAdmin)
admin.site.register(WebmVideo, WebmVideoAdmin)
