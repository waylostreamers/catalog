from django.urls import path, include

from . import views

addpatterns = [
    path("artist/", views.AddArtistView.as_view(), name="add-artist"),
    path("album/", views.AddAlbumView.as_view(), name="add-album"),
    path("track/", views.AddTrackView.as_view(), name="add-track"),
    path("", views.add, name="add"),
]

urlpatterns = [
    path("add/", include(addpatterns)),
    path("browse/", views.browse, name="browse"),
    path("albums/", views.AlbumsView.as_view(), name="albums"),
    path("/album/<slug:pk>/", views.AlbumDetailView.as_view(), name="album-detail"),
    path("/track/<slug:pk>/", views.TrackDetailView.as_view(), name="track-detail"),
    path("/artist/<slug:pk>/", views.ArtistDetailView.as_view(), name="artist-detail"),
    path("artists/", views.ArtistsView.as_view(), name="artists"),
    path("artist_search/", views.artist_search, name="artists-search"),
    path("album_search/", views.album_search, name="albums-search"),
    path("track_search/", views.track_search, name="tracks-search"),
    
    path("tracks/", views.TracksView.as_view(), name="tracks"),
    path("", views.index, name="index"),
]
