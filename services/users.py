import sqlite3


DB_PATH = "data/bot.db"


def init_db():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY
            )
        """)


def subscribe_user(user_id: int):
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,)
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