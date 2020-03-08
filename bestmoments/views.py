"""
"""
from bestmoments.models import BestImage
from django.shortcuts import render


def best_image_list(request):
    """
    """
    images = BestImage.objects.order_by("image")
    template_name = "index.html"
    context = {"page": "bmoments", "images": images}
    return render(request, template_name, context)
