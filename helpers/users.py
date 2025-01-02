import dataclasses
import os


@dataclasses.dataclass
class User:
    firstName: str
    lastName: str
    email: str
    gender: str
    mobile: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: [str]
    hobby: str
    picture: str
    address: str
    state: str
    city: str


picture_path = os.path.abspath(f'../data/cat.jpg')

test_user = User(firstName='John', lastName='Smith', email='JS@amazon.com', gender='Male', mobile='1234567890',
                 birth_day='10', birth_month='October', birth_year='1995', subjects=['Arts', 'Maths'], hobby='Sports',
                 picture=picture_path, address='Street Pyshkina, house Kolotyshnika', state='Haryana', city='Karnal')
