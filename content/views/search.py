from django.shortcuts import render

from ..models import Album, Artist, Track


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
