from django.db import models


class User(models.Model):
    email = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()


class Artist(models.Model):
    name = models.TextField()
    artwork_id = models.UUIDField(null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Role(models.Model):
    description = models.TextField()


class Contributor(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


class Track(models.Model):
    isrc = models.CharField(max_length=12)
    title = models.TextField()
    artists = models.ManyToManyField(Contributor)
    audio_file_id = models.UUIDField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6)
    stream_cost = models.DecimalField(decimal_places=4, max_digits=6)
    purchase_count = models.BigIntegerField(default=0)
    stream_count = models.BigIntegerField(default=0)


class Album(models.Model):
    upc = models.IntegerField()
    title = models.TextField()
    artists = models.ManyToManyField(Contributor)
    tracks = models.ManyToManyField(Track)
    artwork_id = models.UUIDField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6)
    purchase_count = models.BigIntegerField(default=0)
