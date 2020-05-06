"""
"""
from django import forms
from filmlist.models import Film
from wishlist.models import Wish


class WishForm(forms.Form):
    """
    """

    title = forms.CharField(label_suffix="",
                            label="Movie title ",
                            max_length=100)
    username = forms.CharField(label_suffix="",
                               label="\nYour username ",
                               max_length=100)
    film_url = forms.URLField(label_suffix="",
                              label="\nURL to kinopoisk/wiki/etc ",
                              required=False)

    def clean_title(self):
        """
        """
        title = self.cleaned_data.get("title", None)
        if Film.objects.filter(title=title).count() != 0:
            raise forms.ValidationError("Already in film list")
        elif Wish.objects.filter(title=title).count() != 0:
            raise forms.ValidationError("Already in wish list")
        else:
            return title
