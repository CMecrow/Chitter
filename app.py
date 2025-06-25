import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# Albums

@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('record_store.html', albums=albums)

@app.route('/albums/<int:id>')
def get_album_with_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('record.html', album=album)

@app.route('/albums/new')
def get_new_album():
    return render_template('new_record.html')

@app.route('/albums/', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    album = repository.create(album)
    return redirect(url_for('get_albums'))

@app.route('/albums/<int:id>/delete', methods=['POST'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return redirect(url_for('get_albums'))
# Artists

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('record_store.html', artists=artists)

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre']
    )
    repository.create(artist)
    return '', 200


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
