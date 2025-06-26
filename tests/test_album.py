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

def test_album_validity():
    assert Album(1, "", "", "").is_valid() == False
    assert Album(1, "Title", "", "").is_valid() == False
    assert Album(1, "", "2024", "").is_valid() == False
    assert Album(1, "Title", None, "").is_valid() == False
    assert Album(1, None, "2024", "").is_valid() == False
    assert Album(1, "Title", "2024", "8").is_valid() == True
    assert Album(None, "Title", "2024", "7").is_valid() == True

def test_album_validity():
    assert Album(1, "", "", "").generate_errors() == "Title can't be blank, Release Year can't be blank, Artist id can't be blank"
    assert Album(1, "Title", "", "").generate_errors() == "Release Year can't be blank, Artist id can't be blank"
    assert Album(1, "", "2024", "").generate_errors() == "Title can't be blank, Artist id can't be blank"
    assert Album(1, "Title", None, "").generate_errors() == "Release Year can't be blank, Artist id can't be blank"
    assert Album(1, None, "2024", "").generate_errors() == "Title can't be blank, Artist id can't be blank"
    assert Album(1, "Title", "2024", "8").generate_errors() == None
    assert Album(None, "Title", "2024", "7").generate_errors() == None