from collections import defaultdict
from datetime import datetime


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days <= 7:
            day_of_week = birthday_this_year.strftime('%A')

            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")


if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "Steve Jobs", "birthday": datetime(1955, 2, 28)},
        {"name": "Mick Jonson", "birthday": datetime(1969, 3, 2)},
        {"name": "Gose Trise", "birthday": datetime(1969, 2, 27)},
        {"name": "Frank Soulse", "birthday": datetime(1969, 2, 25)},
        {"name": "Test Mister", "birthday": datetime(1969, 3, 1)},
    ]

    get_birthdays_per_week(users)
