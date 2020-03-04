"""
"""
from django.shortcuts import render
from django.http import  HttpRequest
from wishlist.views import wish_list
from filmlist.views import film_list
from filmqueue.views import queue_list

def index_page(request):
    """
    """
    if request.method == "POST":
        print(request.POST)
        if "queue" in request.POST:
            return queue_list(request)
        elif "flist" in request.POST:
            return film_list(request)
        elif "wlist"in request.POST:
            return wish_list(request)
    else:
        return queue_list(request)
