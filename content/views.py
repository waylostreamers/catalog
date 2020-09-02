from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Album, Artist


class AlbumsView(ListView):
    model = Album
    paginate_by = 10
    template_name = "albums.html"


class ArtistsView(ListView):
    model = Artist
    paginate_by = 10
    template_name = "artists.html"


def index(request):
    return render(request, "index.html")
