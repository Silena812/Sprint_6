from faker import Faker
import random

fake = Faker('ru_RU')

def generate_user_data():
    first_name = fake.first_name()
    if len(first_name) < 2:
        first_name += 'а'
    first_name = first_name[:15]

    last_name = fake.last_name()
    if len(last_name) < 2:
        last_name += 'в'

    address = fake.street_address()
    if len(address) < 5:
        address += ' дом'
    address = address[:49]

    return {
        "first_name": first_name,
        "last_name": last_name,
        "address": address,
        "metro_station": random.choice(["Чистые пруды", "Китай-город", "Таганская"]),
        "phone": fake.phone_number(),
        "delivery_date": fake.date_between(start_date="today", end_date="+7d").strftime("%d.%m.%Y"),
        "comment": fake.sentence(nb_words=6)
    }
