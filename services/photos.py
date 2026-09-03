import random
import sqlite3
from typing import Optional

DB_PATH = "data/bot.db"


def add_photo(city: str, photo_file_id: str, uploaded_by: int):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            INSERT INTO city_photos (
                city,
                photo_file_id,
                uploaded_by,
                status
            )
            VALUES (?, ?, ?, 'pending')
            """,
            (city, photo_file_id, uploaded_by)
        )


def get_pending_photo():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            """
            SELECT id, city, photo_file_id, uploaded_by
            FROM city_photos
            WHERE status = 'pending'
            LIMIT 1
            """
        )

        return cursor.fetchone()


def approve_photo(photo_id: int):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            UPDATE city_photos
            SET status = 'approved'
            WHERE id = ?
            """,
            (photo_id,)
        )


def reject_photo(photo_id: int):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            UPDATE city_photos
            SET status = 'rejected'
            WHERE id = ?
            """,
            (photo_id,)
        )


def get_city_photo(city: str) -> Optional[str]:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            """
            SELECT photo_file_id
            FROM city_photos
            WHERE city = ?
            AND status = 'approved'
            """,
            (city,)
        )

        photos = cursor.fetchall()

        if not photos:
            return None

        return random.choice(photos)[0]

def get_city(user_id: int) -> Optional[str]:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            """
            SELECT city
            FROM users
            WHERE user_id = ?
            """,
            (user_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]