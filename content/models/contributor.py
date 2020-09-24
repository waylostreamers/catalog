from django.db import models

from .artist import Artist
from .role import Role


class Contributor(models.Model):
    """
    An artist plays a particular role on an album/track.
    To associate an artist with a track or album,
    we must create a Contributor which defines the artist's role.

    i.e. "Keith Carlock" (Artist) was the "drummer" (Role)
    on "Pistachio" (Album)
    The contributor is (Artist=Keith Carlock, Role=drummer)
    """

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    @property
    def name(self):
        return self.artist.name

    def album(self):
        return self.album_set.first()

    def track(self):
        return self.track_set.first()

    class Meta:
        db_table = 'content"."contributor'
