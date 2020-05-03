from django.db import models


class SoundRecording(models.Model):
    bitrate = models.IntegerField()
    samplerate = models.IntegerField()
    filetype = models.CharField(max_length=12)
    length = models.IntegerField()  # in seconds
    size = models.IntegerField()  # in MB
    channels = models.IntegerField()
    file_id = models.UUIDField()

    class Meta:
        db_table = 'content"."soundrecording'
