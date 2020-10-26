from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import ArtistForm, AlbumForm, TrackForm


class AddAlbumView(LoginRequiredMixin, FormView):
    template_name = "add_album.html"
    form_class = AlbumForm
    success_url = "/add/"


class AddArtistView(LoginRequiredMixin, FormView):
    template_name = "add_artist.html"
    form_class = ArtistForm
    success_url = "/add/"


class AddTrackView(LoginRequiredMixin, FormView):
    template_name = "add_track.html"
    form_class = TrackForm
    success_url = "/add/"
