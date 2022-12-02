from initialize_db import reset_database

def pytest_configure():
    reset_database()