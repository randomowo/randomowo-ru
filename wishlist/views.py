"""
"""
from django.shortcuts import render

from wishlist.forms import WishForm
from wishlist.models import Wish


def wish_list(request):
    """
    """
    added = False
    if request.method == "POST":
        form = WishForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            username = form.cleaned_data["username"]
            film_url = form.cleaned_data["film_url"]
            Wish.objects.create(title=title,
                                username=username,
                                film_url=film_url)
            added = True
    wishes = Wish.objects.order_by("-pub_date")
    template_name = "user/cinema/wlist.html"
    context = {
        "form": WishForm(),
        "wishes": wishes,
        "added": added,
    }
    return render(request, template_name, context)
