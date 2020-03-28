"""
"""
from django.urls import path
from index.views import index_page
from wishlist.views import wish_list
from challenges.views import challenge_list
from filmlist.views import random_film

urlpatterns = [
    path("", index_page, name="index"),
    path("random", random_film, name="random"),
    path("wish", wish_list, name="wish"),
    path("challenges", challenge_list, name="challenges"),
]
