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


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
