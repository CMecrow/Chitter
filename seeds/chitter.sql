DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post_content text,
    post_datetime TIMESTAMP
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (post_content, post_datetime) VALUES ('I wonder if Chitter will ever take off', '2008-11-11 13:23:44')