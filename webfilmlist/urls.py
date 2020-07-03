"""webfilmlist URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from bestmoments.views import best_image_list
from bestmoments.views import webms
from challenges.views import challenge_list
from filmlist.views import film_list
from filmlist.views import random_film
from index.views import yesno
from wishlist.views import wish_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cinema/", film_list, name="film_list"),
    path("cinema/filmlist/", film_list, name="film_list"),
    path("cinema/wishlist/", wish_list, name="wish_list"),
    path("cinema/challenges/", challenge_list, name="challenge_list"),
    path("cinema/random/", random_film, name="random_film"),
    path("cinema/bestmoments/", best_image_list, name="best_image_list"),
    path("yesno/", yesno),
    path("webms/", webms),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
