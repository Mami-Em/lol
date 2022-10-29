CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL UNIQUE,
    password_hash VARCHAR NOT NULL
);

CREATE TABLE user_session (
    userid INT REFERENCES users(id),
    is_active BOOLEAN,
    last_seen TIMESTAMP 
);

CREATE TABLE user_details (
    userid INT REFERENCES users(id),
    email VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE user_history (
    userid INT REFERENCES users(id),
    created_at TIMESTAMP,
    last_updated TIMESTAMP
);

CREATE TABLE convers (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP,
    creator_id INT REFERENCES users(id)
);

CREATE TABLE convers_details (
    id SERIAL PRIMARY KEY,
    conv_id INT REFERENCES convers(id),
    sender_id INT REFERENCES users(id),
    msg VARCHAR NOT NULL
);

CREATE TABLE messages ();