from lib.album import Album
from lib.album_repository import AlbumRepository

def test_get_all_albums(db_connection):
    album_repository = AlbumRepository(db_connection)
    result = album_repository.all()
    assert result == [
        Album(1, "Silent Alarm", 2005, 1),
    ]