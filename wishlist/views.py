"""
"""
from django.shortcuts import render
from wishlist.models import Wish


def wish_list(request):
    """
    """
    print("lolol")
    added = False
    if request.method == "POST":
        name = request.POST.get("name")
        film_url = request.POST.get("film_url")
        username = request.POST.get("username")
        if name and username and Wish.objects.filter(name=name).count() == 0:
            new_wish = Wish(name=name, username=username, film_url=film_url)
            new_wish.save()
            added = True
    wishes = Wish.objects.all()
    template_name = "index.html"
    context = {
        "page": "wlist",
        "wishes": wishes,
        "added": added,
    }
    return render(request, template_name, context)
