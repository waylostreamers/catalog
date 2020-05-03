from django.db import models


class Location(models.Model):
    """
    The address of a location. This could be used
    for artist locations, recording studios etc.
    """

    address_one = models.CharField(max_length=256, null=True)
    address_two = models.CharField(max_length=256, null=True)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    latitude = models.DecimalField(max_digits=24, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=24, decimal_places=15, null=True)
    phone_number = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'content"."location'
