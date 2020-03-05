"""
"""
from django import forms


class WishForm(forms.Form):
    """
    """

    title = forms.CharField(label="Movie title ", max_length=100)
    username = forms.CharField(label="\nYour username ", max_length=100)
    film_url = forms.URLField(label="\nURL to kinopoisk/wiki/etc ",
                              required=False)
