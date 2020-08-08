"""
"""
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from filmlist.models import Film


def get_films(request):
    """
    """
    if request.method == "GET":
        count = int(request.GET.get("count", 30))
        start = int(request.GET.get("start", 0))
        films = Film.objects.order_by("is_watched", "title")[start:start+count]
        response = []
        for film in films:
            film_json = {
                "id": film.pk,
                "title": film.title,
                "year": film.year,
                "director": film.director,
                "url": film.url,
                "is_watched": film.is_watched,
                "is_movie": film.is_movie,
                "seasons": [],
            }
            for season, episodes in film.serial:
                film_json["seasons"].append({
                    "id": season.pk,
                    "number": season.number,
                    "episodes": [{
                        "id": episode.pk,
                        "title": episode.title,
                        "number": episode.number,
                        "duration": episode.duration,
                        "is_watched": episode.is_watched,
                    } for episode in episodes]
                })
            response.append(film_json)
        return JsonResponse(json.dumps(response), safe=False)
    else:
        return HttpResponse(status=403)


def search_films(request):
    """
    """
    pass
