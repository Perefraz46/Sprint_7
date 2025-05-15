from faker import Faker

fake = Faker('ru_RU')

def order_data():
    payload_order = {
        "firstName": fake.first_name_male(),
        "lastName": fake.last_name_male(),
        "address": "Москва, ул. Карла Маркса 145",
        "metroStation": 4,
        "phone": "+7 981 555 44 33",
        "rentTime": 5,
        "deliveryDate": str(fake.future_date()),
        "comment": "Йо-хо-хо!!!",
        "color": [
            "BLACK"
        ]
    }
    return payload_order

class ErrorMessages:

    DUPLICATE_LOGIN = "Этот логин уже используется. Попробуйте другой."
    INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"
