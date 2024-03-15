from datetime import datetime, timedelta

def find_next_weekday(date, weekday):
    days_until_next_weekday = (weekday - date.weekday()) % 7
    if days_until_next_weekday == 0:
        days_until_next_weekday = 7
    return date + timedelta(days=days_until_next_weekday)

def get_upcoming_birthdays(prepared_users, days=7):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.03.22"}
]

prepared_users = [
    {"name": "John Doe", "birthday": datetime.strptime("1985.01.23", '%Y.%m.%d').date()},
    {"name": "Jane Smith", "birthday": datetime.strptime("1990.01.27", '%Y.%m.%d').date()}
]

upcoming_birthdays = get_upcoming_birthdays(prepared_users)
print("Список майбутніх днів народження:", upcoming_birthdays)