import sqlite3
from datetime import date

DB_PATH = "data/bot.db"

DEFAULT_DEPARTURE_DATE = date(2026, 12, 27)


def init_db():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                departure_date TEXT NOT NULL
            )
        """)


def subscribe_user(user_id: int):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            INSERT OR IGNORE INTO users (user_id, departure_date)
            VALUES (?, ?)
            """,
            (user_id, DEFAULT_DEPARTURE_DATE.isoformat())
        )


def unsubscribe_user(user_id: int):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            "DELETE FROM users WHERE user_id = ?",
            (user_id,)
        )


def get_subscribed_users() -> list[int]:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute("SELECT user_id FROM users")
        return [row[0] for row in cursor.fetchall()]


def get_departure_date(user_id: int):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.execute(
            "SELECT departure_date FROM users WHERE user_id = ?",
            (user_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]


def set_departure_date(user_id: int, departure_date: str):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """
            UPDATE users
            SET departure_date = ?
            WHERE user_id = ?
            """,
            (departure_date, user_id)
        )