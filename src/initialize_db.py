from database import db
from app import create_app

app = create_app()
app.app_context().push()


def create_tables():
    db.session.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT,
            password TEXT
        );
    """)

    db.session.execute("""
        CREATE TABLE citations (
            id SERIAL PRIMARY KEY,
            owner_id INTEGER REFERENCES users,
            given_id INTEGER,
            type TEXT
        );
    """)
    db.session.commit()

    db.session.execute("""
    CREATE TABLE books (
        id SERIAL PRIMARY KEY,
        owner_id TEXT,
        given_id TEXT,
        author TEXT,
        editor TEXT,
        title TEXT,
        publisher TEXT,
        year INTEGER
    );
    """)
    db.session.commit()

    db.session.execute("""
    CREATE TABLE articles (
        id SERIAL PRIMARY KEY,
        owner_id TEXT,
        given_id TEXT,
        author TEXT,
        title TEXT,
        journal TEXT,
        year INTEGER
    );
    """)
    db.session.commit()

    db.session.execute("""
    CREATE TABLE othercitations (
        id SERIAL PRIMARY KEY,
        owner_id TEXT,
        given_id TEXT,
        author TEXT,
        title TEXT,
        type TEXT,
        other TEXT,
        year INTEGER
    );
    """)
    db.session.commit()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users CASCADE;
    """)

    db.session.execute("""
        DROP TABLE IF EXISTS citations CASCADE;
    """)
    db.session.commit()

    db.session.execute("""
        DROP TABLE IF EXISTS books CASCADE;
    """)
    db.session.commit()

    db.session.execute("""
        DROP TABLE IF EXISTS articles CASCADE;
    """)
    db.session.commit()

    db.session.execute("""
        DROP TABLE IF EXISTS othercitations CASCADE;
    """)
    db.session.commit()


def reset_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    reset_database()
