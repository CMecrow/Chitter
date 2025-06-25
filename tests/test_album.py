from lib.album import Album

def test_album():
    album = Album(1, 'Test title', 2025, 1)
    assert album.id == 1
    assert album.title == 'Test title'
    assert album.release_year == 2025
    assert album.artist_id == 1

def test_equality():
    album1 = Album(1, 'Test title', 2025, 1)
    album2 = Album(1, 'Test title', 2025, 1)
    assert album1 == album2

def test_stringy_albums():
    album = Album(1, 'Test title', 2025, 1)
    assert str(album) == "Album(1, Test title, 2025, 1)"