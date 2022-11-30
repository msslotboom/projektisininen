from app import app
import psycopg2
import os
from repositories.user_repository import user_repository

if __name__ == "__main__":
    
    conn = psycopg2.connect(
        dbname=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASS"),
        host=os.environ.get("POSTGRES_HOST"),
        port=os.environ.get("POSTGRES_PORT")
    )
    cursor = conn.cursor()
    cursor.execute(open("schema.sql", "r").read())

    app.run()

    cursor.close()
    
    conn.close()
