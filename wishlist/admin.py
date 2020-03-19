"""
"""
from django.contrib import admin
from wishlist.models import Wish


class WishAdmin(admin.ModelAdmin):
    """
    """

    list_display = ["title"]


admin.site.register(Wish, WishAdmin)
