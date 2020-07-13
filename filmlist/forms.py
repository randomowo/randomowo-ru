"""
"""
from challenges.models import Challenge
from challenges.models import FilmChallenge
from django import forms
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.forms.models import inlineformset_factory
from filmlist.models import Film
from filmlist.models import Season
from filmlist.models import Episode


class FilmAdminForm(forms.ModelForm):
    """
    """

    def clean_title(self):
        """
        """
        title = self.cleaned_data.get("title", None)
        year = self.data.get("year", None)
        film = Film.objects.filter(title=title).first()
        print(self.changed_data)
        if film and film.year == int(year) and "title" in self.changed_data:
            raise forms.ValidationError("Film already exist")
        else:
            return title

    class Meta:
        models = Film


class SeasonAdminForm(forms.ModelForm):
    """
    """
    def __init__(self, *args, **kwargs):
        super(SeasonAdminForm, self).__init__(*args, **kwargs)
        self.fields["film"] = forms.ModelChoiceField(
            queryset=Film.objects.filter(is_movie=False))


class RandomForm(forms.Form):
    """
    """

    OPTIONS = [
        ("all", "all"),
        ("watched", "watched"),
        ("unwatched", "unwatched"),
    ]
    for ch in Challenge.objects.all():
        OPTIONS.append((f"ch_{ch.id}", ch.task))

    filter_choice = forms.ChoiceField(required=False,
                                      choices=OPTIONS,
                                      label="",
                                      initial="unwatched")
