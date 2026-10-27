from datetime import date, datetime
from zoneinfo import ZoneInfo

from services.users import get_departure_date, START_EDUCATION_TIME


def get_days_left(user_id: int) -> int:
    departure_date = get_departure_date(user_id)

    if departure_date is None:
        return 0

    departure_date = date.fromisoformat(departure_date)
    today = datetime.now(ZoneInfo("Europe/Moscow")).date()

    return (departure_date - today).days

def get_already_days_left() -> int:
    today = datetime.now(ZoneInfo("Europe/Moscow")).date()

    return (today - START_EDUCATION_TIME).days

def get_whole_days(user_id: int) -> int:
    departure_date = get_departure_date(user_id)
    if departure_date is None:
        return 0

    departure_date = date.fromisoformat(departure_date)
    return (departure_date - START_EDUCATION_TIME).days
