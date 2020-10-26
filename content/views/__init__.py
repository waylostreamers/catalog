from .basics import (
    index,
    browse,
    add,
)
from .add_content import (
    AddAlbumView,
    AddArtistView,
    AddTrackView,
)
from .details import (
    AlbumDetailView,
    TrackDetailView,
    ArtistDetailView,
)
from .lists import (
    AlbumsView,
    ArtistsView,
    TracksView,
)
from .search import (
    artist_search,
    album_search,
    track_search,
)
from .login import WayloLoginView, WayloLogoutView
from .profile import user_profile_view
