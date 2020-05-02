from django.db import models

from .user import User


class RightsAgreement(models.Model):

    agreement_name = models.TextField()
    agreement_date = models.DateField()
    owner = models.ManyToManyField(User)
