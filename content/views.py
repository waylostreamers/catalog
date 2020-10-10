from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from .models import Album, Artist, Track
from .forms import ArtistForm, AlbumForm, TrackForm


class AlbumsView(ListView):
    model = Album
    paginate_by = 10
    template_name = "albums.html"


class AlbumDetailView(DetailView):
    model = Album
    template_name = "album.html"


class TrackDetailView(DetailView):
    model = Track
    template_name = "track.html"


class ArtistDetailView(DetailView):
    model = Artist
    template_name = "artist.html"


class AddAlbumView(FormView):
    template_name = "add_album.html"
    form_class = AlbumForm
    success_url = "/add/"


class ArtistsView(ListView):
    model = Artist
    paginate_by = 10
    template_name = "artists.html"


class AddArtistView(FormView):
    template_name = "add_artist.html"
    form_class = ArtistForm
    success_url = "/add/"


class TracksView(ListView):
    model = Track
    paginate_by = 20
    template_name = "tracks.html"


class AddTrackView(FormView):
    template_name = "add_track.html"
    form_class = TrackForm
    success_url = "/add/"


def artist_search(request):
    """ This could be your actual view or a new one """
    if request.method == "GET":  # If the form is submitted
        search_query = request.GET.get("artist_search", None)
        result = Artist.objects.filter(alias__name__contains=search_query).distinct()
        return render(request, "artist_search.html", {"stuff": result})


def album_search(request):
    """ This could be your actual view or a new one """
    if request.method == "GET":  # If the form is submitted
        search_query = request.GET.get("album_search", None)
        result = Album.objects.filter(title__contains=search_query).distinct()
        return render(request, "album_search.html", {"stuff": result})


def track_search(request):
    """ This could be your actual view or a new one """
    if request.method == "GET":  # If the form is submitted
        search_query = request.GET.get("track_search", None)
        result = Track.objects.filter(title__contains=search_query).distinct()
        return render(request, "track_search.html", {"stuff": result})


def index(request):
    return render(request, "index.html")


def browse(request):
    return render(request, "browse.html")


def add(request):
    return render(request, "add.html")
