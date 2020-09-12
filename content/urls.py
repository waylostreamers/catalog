from django.urls import path

from . import views


urlpatterns = [
    path("albums/", views.AlbumsView.as_view(), name="albums"),
    path("artists/", views.ArtistsView.as_view(), name="artists"),
    path("tracks/", views.TracksView.as_view(), name="tracks"),
    path("", views.index, name="index"),
]
