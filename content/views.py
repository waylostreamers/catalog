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
    ''' This could be your actual view or a new one '''
    # Your code
    #from django.db.models import Q
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('artist_search', None)
        #result = Artist.objects.filter(Q(owner__first_name__contains='a') | Q(owner__last_name__contains='a'))
        #result = Artist.objects.filter(owner__first_name__contains=search_query)
        #result = Artist.objects.filter(owner__first_name__contains=search_query)
        #result = Artist.objects.filter(artist().name=search_query)

        filtered = (x for x in Artist.objects.all() if search_query in x.name())
        filtered_dict  = {'user_data': filtered}
        #for p in Artist.raw('SELECT owner FROM myapp_artist where ')
        # Do whatever you need with the word the user looked for
        #result = Artist.other_aliases(name__contains=search_query)
        #return render(result, "artist_search.html")
        return render(request, "artist_search.html", { "stuff": filtered_dict })


def index(request):
    return render(request, "index.html")

def browse(request):
    return render(request, "browse.html")

def add(request):
    return render(request, "add.html")
