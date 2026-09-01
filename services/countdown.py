from datetime import date
import json

departure_time = date(2026, 11, 27)


def get_days_left() -> int:
    return (departure_time - date.today()).days