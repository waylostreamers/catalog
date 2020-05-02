from django.db import models

from .location import Location

class User(models.Model):
    """
    An uploader (band or a label or an artist)
    """
    email = models.EmailField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
