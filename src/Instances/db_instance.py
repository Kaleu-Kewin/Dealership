import os
from ..Database import Database

db = Database(
    os.getenv("DB_HOST"),
    os.getenv("DB_NAME"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASSWORD"),
    os.getenv("DB_PORT")
)

db.conectar()