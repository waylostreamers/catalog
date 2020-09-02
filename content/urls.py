from django.urls import path

from . import views


urlpatterns = [
    path("albums/", views.AlbumsView.as_view(), name="albums"),
    path("artists/", views.ArtistsView.as_view(), name="artists"),
    path("", views.index, name="index"),
]
