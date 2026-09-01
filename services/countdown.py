from datetime import date, datetime
from zoneinfo import ZoneInfo

departure_date = date(2026, 12, 27)


def get_days_left() -> int:
    today = datetime.now(ZoneInfo("Europe/Moscow")).date()
    return (departure_date - today).days


def change_departure_date(new_date: date) -> None:
    global departure_date
    departure_date = new_date