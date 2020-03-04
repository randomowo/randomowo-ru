"""
"""
from django.urls import path

from wishlist.views import wish_list

urlpatterns = [
    path("", wish_list, name="wish-list"),
]
