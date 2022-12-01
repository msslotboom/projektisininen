CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS citations (
    id INTEGER PRIMARY KEY,
    authors TEXT,
    title TEXT,
    year INTEGER
);