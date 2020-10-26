from django.views.generic.detail import DetailView

from ..models import Album, Artist, Track


class AlbumDetailView(DetailView):
    model = Album
    template_name = "album.html"


class TrackDetailView(DetailView):
    model = Track
    template_name = "track.html"


class ArtistDetailView(DetailView):
    model = Artist
    template_name = "artist.html"
