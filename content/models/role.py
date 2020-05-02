from django.db import models


class Role(models.Model):
    """
    A description of the action that an artist
    may perform on a track or album.
    For example,
        | If you are the producer then please
        | produce us a bottle of decent chardonnay.
    """

    PRIMARY = "PRIMARY"
    FEATURED = "FEATURED"
    WRITER = "WRITER"
    PRODUCER = "PRODUCER"
    COMPOSER = "COMPOSER"
    SINGER = "SINGER"
    PIANIST = "PIANIST"
    KEYBOARDIST = "KEYBOARDIST"
    DRUMMER = "DRUMMER"
    LAGERPHONIST = "LAGERPHONIST"
    LYRICIST = "LYRICIST"
    PUBLICIST = "PUBLICIST"
    STYLIST = "STYLIST"
    KEY_GRIP = "KEY_GRIP"
    MANAGER = "MANAGER"
    CONCEPTUALIST = "CONCEPTUALIST"
    GUITARIST = "GUITARIST"
    SYNTHESIST = "SYNTHESIST"

    CHOICES = [
        (PRIMARY, "Primary Artist"),
        (FEATURED, "Featured Artist"),
        (WRITER, "Writer"),
        (PRODUCER, "Producer"),
        (COMPOSER, "Composer"),
        (SINGER, "Singer"),
        (PIANIST, "Pianist"),
        (KEYBOARDIST, "Keyboardist"),
        (DRUMMER, "Drummer"),
        (LAGERPHONIST, "Lagerphonist"),
        (LYRICIST, "Lyricist"),
        (PUBLICIST, "Publicist"),
        (STYLIST, "Stylist"),
        (KEY_GRIP, "Key Grip"),
        (MANAGER, "Manager"),
        (CONCEPTUALIST, "Conceptualist"),
        (GUITARIST, "Guitarist"),
        (SYNTHESIST, "Synthesist"),
    ]

    description = models.CharField(max_length=256, choices=CHOICES, default=PRIMARY)
