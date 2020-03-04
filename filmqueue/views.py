"""
"""
from django.shortcuts import render
from filmqueue.models import FilmQueue

def queue_list(request):
    """
    """
    queue = FilmQueue.objects.order_by("id")
    template_name = "index.html"
    context = {
        "page": "queue",
        "queue": queue,
    }
    return render(request, template_name, context)
