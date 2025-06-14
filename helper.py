from faker import Faker
import random

fake = Faker('ru_RU')
def generate_metro_search_term(full_station_name):

    length = 3 if len(full_station_name) >= 3 else len(full_station_name)
    return full_station_name[:length]

def generate_user_data():
    first_name = fake.first_name()
    if len(first_name) < 2:
        first_name += 'а'
    first_name = first_name[:15]

    last_name = fake.last_name()
    if len(last_name) < 2:
        last_name += 'в'

    stations = ["Чистые пруды", "Лубянка", "Таганская"]
    station_full = random.choice(stations)
    station_search = station_full[:4]
    return {
        "first_name": first_name,
        "last_name": last_name,
        "address": 'тестовый адрес 123',
        "metro_station_search": station_search,
        "metro_station_full": station_full,
        "phone": '88888888888',
        "date": fake.date_between(start_date="+1d", end_date="+7d").strftime("%d.%m.%Y"),
        "period_text": random.choice([
            "сутки", "двое суток", "трое суток",
            "четверо суток", "пятеро суток", "шестеро суток"
        ]),
        "color": random.choice(["black", "grey"]),
        "comment": fake.sentence(nb_words=6)
    }
