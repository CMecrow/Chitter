from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.

def test_artist_validity():
    assert Artist(1, "", "").is_valid() == False
    assert Artist(1, "Title", "").is_valid() == False
    assert Artist(1, "", "Author").is_valid() == False
    assert Artist(1, "Title", None).is_valid() == False
    assert Artist(1, None, "Author").is_valid() == False
    assert Artist(1, "Title", "Author").is_valid() == True
    assert Artist(None, "Title", "Author").is_valid() == True

def test_artist_errors():
    assert Artist(1, "", "").generate_errors() == "Artist name can't be blank, Genre can't be blank"
    assert Artist(1, "Title", "").generate_errors() == "Genre can't be blank"
    assert Artist(1, "", "Author").generate_errors() == "Artist name can't be blank"
    assert Artist(1, "Title", None).generate_errors() == "Genre can't be blank"
    assert Artist(1, None, "Author").generate_errors() == "Artist name can't be blank"
    assert Artist(1, "Title", "Author").generate_errors() == None
    assert Artist(None, "Title", "Author").generate_errors() == None