from django.db import models

'''
an uploader ( band or a label or an artist )

'''
class User(models.Model):
    email = models.EmailField()
    #first_name = models.TextField()
    first_name = models.CharField(max_length = 256)
    #last_name = models.TextField()
    last_name = models.CharField(max_length = 256)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)

'''
artist + role = contributor 

artist: steelyAI band 
role : primary artists 
contributor : { artist: steelyAI, role : primary artist } 

'''
'''
artist has an owner ( a user ) . could be label manager 
'''
class Artist(models.Model):
    #name = models.TextField() #no need for such a large field . I assume CharField will make faster performance
    name = models.CharField(max_length = 256)
    artwork_id = models.UUIDField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    birth_location = models.CharField(max_length = 256)
    current_location = models.CharField(max_length = 256)
    gender = models.CharField(max_length = 256)
    nationality = models.CharField(max_length = 256)
   # related_artists = models.ArrayField(models.CharField(max_length=100))
    artist_url = models.TextField() # ( www.waylostreams.com/seanwayland )
    external_urls = models.ArrayField(models.CharField(max_length=256)) # ( ['www.seanwayland.com','facebook/sean']  )

'''
basically a description of the action that an artist performed on a track or album ie the producer 
" if you are the producer then please produce us a bottle of decent chardonnay " 
'''
class Role(models.Model):


    description = models.CharField(max_length=256) # ( "producer" , "engineer" )

'''
a combination of artists and role can be added to an album .. ie keith carlock played drums on pistachio 

'''
class Contributor(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)


class Track(models.Model):
    isrc = models.CharField(max_length=12)
    #title = models.TextField()
    title = models.CharField(max_length = 256)
    # I think it makes sense to have a text field for artist attached to the track
    #display_artist = models.CharField(max_length = 256)
    artists = models.ManyToManyField(Contributor)
    audio_file_id = models.UUIDField()
    track_url = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6)
    stream_cost = models.DecimalField(decimal_places=4, max_digits=6)
    purchase_count = models.BigIntegerField(default=0)
    stream_count = models.BigIntegerField(default=0)
    track_credits = models.TextField()
    artwork_id = models.UUIDField()
    genres = models.TextField()
    '''
    bitrate, sampleriate, filetype, length, size , interleaved / mono
    https://github.com/sshaw/ddex/blob/master/lib/ddex/ern/v35/technical_sound_recording_details.rb
    '''
    technical_sound_recording_details = models.TextField()
        # url is either a store of the location in say an s3 bucket or a link to the track on waylostreams



class Album(models.Model):
    upc = models.IntegerField()

    # I think it makes sense to have a text field for artist attached to the album
    #display_artist = models.CharField(max_length = 256)
    #title = models.TextField()
    title = models.CharField(max_length = 256)
    # this is actually titles (plural) in ddex
    '''
    Waiata is the sixth studio album by New Zealand new wave band Split Enz, released in 1981.
     Its Australian release was titled Corroboree. Waiata is the Māori term for song and singing, 
     while corroboree is the Aboriginal term.
    '''
    release_date = models.DateField()
    upload_date = models.DateField()
    remaster_date = models.DateField()
    start_date_time = models.DateField()
    artists = models.ManyToManyField(Contributor)
    tracks = models.ManyToManyField(Track)
    artwork_id = models.UUIDField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_cost = models.DecimalField(decimal_places=4, max_digits=6)
    purchase_count = models.BigIntegerField(default=0)
    # is a label a user or a contributor ?
    label_name = models.CharField()
    album_credits = models.TextField()
    rights_agreement = models.ManyToManyField(Rights_Agreement)
    genres=  models.ManyToManyField(Genre)

    # let's assume this one is a formatted string

    available_markets = models.ArrayField(models.CharField(max_length=10))


class Genre(models.Model):

    genre_name = models.CharField(max_length = 256)

class Rights_Agreement(models.Model):

    agreement_name = models.TextField()
    agreement_date = models.DateField()
    agreement_owner = models.ManyToManyField(User)


class Locations(models.Model):

    address_one = models.CharField(max_length = 256)
    address_two = models.CharField(max_length = 256)
    country = models.CharField(max_length = 100)
    country_code = models.CharField(max_length = 10)
    zip_code =  models.CharField(max_length = 100)
    city =models.CharField(max_length = 100)
    coords = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)


# class labels ?






