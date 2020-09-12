from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Album, Artist, Track


class AlbumsView(ListView):
    model = Album
    paginate_by = 10
    template_name = "albums.html"


class ArtistsView(ListView):
    model = Artist
    paginate_by = 10
    template_name = "artists.html"

class TracksView(ListView):
    model = Track
    paginate_by = 10
    template_name = "tracks.html"


def index(request):
    return render(request, "index.html")
