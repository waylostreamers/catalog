from django.db import models


class User(models.Model):
    """
    An uploader (band or a label or an artist)
    """
    email = models.EmailField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    # location = models.ForeignKey(Locations, on_delete=models.CASCADE)
