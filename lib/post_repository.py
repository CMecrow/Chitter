from lib.post import Post

class PostRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        return [
            Post(row["id"], row["post_content"], row["post_datetime"])
            for row in rows
        ]

    def create(self, post):
        self._connection.execute(
            "INSERT INTO posts (post_content, post_datetime)" \
            "VALUES (%s, %s)", [post.post_content, post.post_datetime]
        )
        return None