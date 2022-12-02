import os
from dotenv import load_dotenv

directory = os.path.dirname(__file__)

load_dotenv(dotenv_path=os.path.join(directory, "..", ".env"))

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
