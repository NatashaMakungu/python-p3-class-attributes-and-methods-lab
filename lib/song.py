class Song:
    pass
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.update_collection(self)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1

    @classmethod
    def update_collection(cls, song):
        cls.add_song_to_count()
        cls.add_to_genres(song.genre)
        cls.add_to_artists(song.artist)
        cls.add_to_genre_count(song.genre)
        cls.add_to_artist_count(song.artist)

ninety_nine_problems = Song("Halo", "Beyonce", "Pop")
print(Song.count)  # => 1
print(Song.genres)  # => ['Pop']
print(Song.artists)  # => ['Beyonce']
print(Song.genre_count)  # => {'Pop': 1}
print(Song.artist_count)  # => {'Beyonce': 1}


