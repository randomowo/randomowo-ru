"""
"""
from challenges.views import challenge_list
from django.urls import path
from filmlist.views import random_film
from index.views import index_page
from wishlist.views import wish_list

urlpatterns = [
    path("", index_page, name="index"),
    path("random", random_film, name="random"),
    path("wish", wish_list, name="wish"),
    path("challenges", challenge_list, name="challenges"),
]
