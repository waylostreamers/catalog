from django import forms

from .models import Artist, Album, Track


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        # fields = []
        fields = "__all__"
        exclude = ["artwork_id"]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = []


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = []
