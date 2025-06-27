_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter
```

```
Nouns: message, post_datetime, username, password

```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                            |
| --------------------- | -------------------                   |
| users                 | username, password                    |
| posts                 | user_id, post_content, post_datetime  |

Name of the table (always plural): `users`

Column names: `title`, `release_year`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Users
id: SERIAL
username: text
password: text

Posts:
id: SERIAL
post_content: text
post_datetime: datetime
user_id: int
```
Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one user have many posts? (Yes)
Can one post have many users? (No)
You'll then be able to say that:

user has many posts
And on the other side, post belongs to user
In that case, the foreign key is in the post table (user_id)
Replace the relevant bits in this example with your own:



## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  password text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  post_content text,
  post_datetime datetime,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 chitter_db < seeds/chitter.sql
```


# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Albums route
GET /albums
Expected response - 200
Album(1, Silent Alarm, 2008, 1)


# Submit album route
POST /album
  title: string
  release_year: string (number)
  artist_id: string (number)

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# GET /wave?name=Leo
#  Expected response (200 OK):
"""
I am waving at Leo
"""

# GET /wave
#  Expected response (200 OK):
"""
I am waving at no one!
"""

# POST /submit
#  Parameters:
#    name: Leo
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you sent this message: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
# def test_get_home(web_client):
#     response = web_client.get('/home')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
# def test_post_submit(web_client):
#     response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```
