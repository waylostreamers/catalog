from django.db import models
from django.utils.functional import cached_property

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


class Role(models.Model):
    """
    A description of the action that an artist may perform on a track or album. For example,
    "If you are the producer then please produce us a bottle of decent chardonnay."

    """

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

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'content"."role'


class Roles:
    @cached_property
    def PRIMARY(self):
        return Role.objects.get(description=PRIMARY)

    @cached_property
    def FEATURED(self):
        return Role.objects.get(description=FEATURED)

    @cached_property
    def WRITER(self):
        return Role.objects.get(description=WRITER)

    @cached_property
    def PRODUCER(self):
        return Role.objects.get(description=PRODUCER)

    @cached_property
    def COMPOSER(self):
        return Role.objects.get(description=COMPOSER)

    @cached_property
    def SINGER(self):
        return Role.objects.get(description=SINGER)

    @cached_property
    def PIANIST(self):
        return Role.objects.get(description=PIANIST)

    @cached_property
    def KEYBOARDIST(self):
        return Role.objects.get(description=KEYBOARDIST)

    @cached_property
    def DRUMMER(self):
        return Role.objects.get(description=DRUMMER)

    @cached_property
    def LAGERPHONIST(self):
        return Role.objects.get(description=LAGERPHONIST)

    @cached_property
    def LYRICIST(self):
        return Role.objects.get(description=LYRICIST)

    @cached_property
    def PUBLICIST(self):
        return Role.objects.get(description=PUBLICIST)

    @cached_property
    def STYLIST(self):
        return Role.objects.get(description=STYLIST)

    @cached_property
    def KEY_GRIP(self):
        return Role.objects.get(description=KEY_GRIP)

    @cached_property
    def MANAGER(self):
        return Role.objects.get(description=MANAGER)

    @cached_property
    def CONCEPTUALIST(self):
        return Role.objects.get(description=CONCEPTUALIST)

    @cached_property
    def GUITARIST(self):
        return Role.objects.get(description=GUITARIST)

    @cached_property
    def SYNTHESIST(self):
        return Role.objects.get(description=SYNTHESIST)
