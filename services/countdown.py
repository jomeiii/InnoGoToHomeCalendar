from datetime import date

departure_date = date(2026, 11, 27)


def get_days_left() -> int:
    return (departure_date - date.today()).days

def change_departure_time(new_date: date) -> None:
    global departure_date
    departure_date = new_date