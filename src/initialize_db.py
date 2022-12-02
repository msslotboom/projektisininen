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
            authors TEXT,
            title TEXT,
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


def reset_database():
    drop_tables()
    create_tables()


if __name__ == "__main__":
    reset_database()
