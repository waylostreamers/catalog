from faker import Faker

from ..models import Artist, Alias

fake = Faker()


def create_user_artists(user):
    """
    Given a user, we should generate a number of artists
    that will appear as contributors on compositions, tracks
    and albums administered by that user.
    """


def create_artist(user, is_user=False):
    artist = Artist(owner=user)
    artist.save()
    default_alias = create_alias(artist)
    if fake.boolean(chance_of_getting_true=25):
        # A small number of artists have a second alias,
        # which is their initials.
        alt_alias = create_alias(artist, alias_of=default_alias)
    return artist


def create_alias(artist, alias_of=None):
    if type(alias_of) is Alias:
        name = alias_of.name
        alias = Alias(name=get_initials(name), default=False, artist=artist)
    else:
        alias = Alias(name=fake.name(), default=True, artist=artist)
    alias.save()
    return alias


def get_initials(name):
    """
    This function takes a string and replaces
    each word before the last word with its initial.
    For example:
    Johann Sebastian Bach -> J.S. Bach
    """
    names = name.split(" ")
    if len(names) < 2:
        raise ValueError("Cannot create initials for single word name")
    given_names = names[0:-1]
    last_name = names[-1]
    initials = ""
    for name in given_names:
        initials = "".join([initials, f"{name[0].upper()}."])
    initials = "".join([initials, f" {last_name.capitalize()}"])
    return initials
