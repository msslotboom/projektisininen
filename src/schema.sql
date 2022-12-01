CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS citations (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER REFERENCES users, 
    authors TEXT,
    title TEXT,
    year INTEGER
);