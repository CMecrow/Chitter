import os
from flask import Flask, request, render_template, redirect, url_for, flash, session
from lib.database_connection import get_flask_database_connection
from lib.post_repository import PostRepository
from lib.post import Post
from lib.user import User
from lib.login import LoginSystem
from datetime import datetime



# Create a new Flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_system = LoginSystem()

def time_stamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# == Your Routes Here ==

@app.route('/posts')
def get_chitter():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    posts = repository.all()
    username = session.get('username')
    return render_template('chitter/index.html', posts=posts, username=username)

@app.route('/posts/new')
def get_new_post():
    return render_template('chitter/new_post.html')

@app.route('/posts', methods=['POST'])
def post_post():
    connection = get_flask_database_connection(app)
    repository = PostRepository(connection)
    post_content = request.form.get('post_content')
    post_time = time_stamp()
    post = Post(None, post_content, post_time)
    if not post.is_valid():
        return render_template('chitter/new_post.html', errors=post.generate_errors()), 400
    new_post = repository.create(post)
    flash("Post added!")
    return redirect(url_for('get_chitter'))

@app.route('/login', methods=['GET', 'POST'])
def post_login():
    if request.method == 'GET':
        return render_template('chitter/login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    user_login = User(username, password)
    if not user_login.is_valid():
        return render_template('chitter/login.html', user=user_login, errors=user_login.generate_errors()), 400
    if user_login not in login_system.users:
        return render_template('chitter/login.html', user=user_login, errors="Incorrect Username or Password"), 401
    login_system.login(user_login)
    session['username'] = username
    return redirect(url_for('get_chitter'))

@app.route('/register', methods=['POST', 'GET'])
def post_register():
    if request.method == 'GET':
        return render_template('chitter/register.html')
    username = request.form.get('username')
    password = request.form.get('password')
    user_login = User(username, password)
    if not user_login.is_valid():
        return render_template('chitter/register.html', user=user_login, errors=user_login.generate_errors()), 400
    if user_login in login_system.users:
        flash("You already have an account!")
        return render_template('chitter/index.html', user=user_login), 401
    login_system.register(user_login)
    flash("You're now registered!")
    return redirect(url_for('get_chitter'))

# Albums

# @app.route('/albums')
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     albums = repository.all()
#     return render_template('record_store.html', albums=albums)

# @app.route('/albums/<int:id>')
# def get_album_with_id(id):
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album = repository.find(id)
#     return render_template('record.html', album=album)

# @app.route('/albums/new')
# def get_new_album():
#     return render_template('new_record.html')

# @app.route('/albums/', methods=['POST'])
# def post_album():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     title = request.form['title']
#     release_year = request.form['release_year']
#     artist_id = request.form['artist_id']
#     album = Album(None, title, release_year, artist_id)
#     if not album.is_valid():
#         return render_template('new_record.html', album=album, errors=album.generate_errors()), 400
#     album = repository.create(album)
#     return redirect(url_for('get_albums'))

# @app.route('/albums/<int:id>/delete', methods=['POST'])
# def delete_album(id):
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     repository.delete(id)
#     return redirect(url_for('get_albums'))

# # Artists

# @app.route('/artists')
# def get_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artists = repository.all()
#     return render_template('record_store.html', artists=artists)

# @app.route('/artists/new')
# def get_new_artist():
#     return render_template('new_artist.html')

# @app.route('/artists/', methods=['POST'])
# def post_artists():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     name = request.form['name']
#     genre = request.form['genre']
#     artist = Artist(None, name, genre)
#     if not artist.is_valid():
#         return render_template('new_artist.html', artist=artist, errors=artist.generate_errors()), 400
#     artist = repository.create(artist)
#     return redirect(url_for('get_artists'))

# @app.route('/artists/<int:id>')
# def get_artist_with_id(id):
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist = repository.find(id)
#     return render_template('artist.html', artist=artist)

# @app.route('/artists/<int:id>/delete', methods=['POST'])
# def delete_artist(id):
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     repository.delete(id)
#     return redirect(url_for('get_artists'))



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
