import os
from selene import browser, be, have, command
from helpers.pages.registration_page import RegistrationPage

firstName = 'John'
lastName = 'Smith'
email = 'JS@amazon.com'
gender = 'Male'
mobile = '1234567890'
birth_day = '10'  # format XX
birth_month = 'October'
birth_year = '1995'
subject1 = 'Arts'
subject2 = 'Maths'
hobby = 'Sports'
picture = 'cat.jpg'
address = 'Street Pyshkina, house Kolotyshnika'
state = 'Haryana'
city = 'Karnal'
picture_path = os.path.abspath(f'../data/{picture}')


def test_registration_form():
    registration_form = RegistrationPage()
    registration_form.open()

    registration_form.fill_firstName(firstName)
    registration_form.fill_lastName(lastName)
    registration_form.fill_email(email)
    registration_form.fill_gender(gender)
    registration_form.fill_mobile(mobile)
    registration_form.fill_birthday(birth_day, birth_month, birth_year)
    registration_form.fill_subjects(subject1, subject2)
    registration_form.fill_hobbby(hobby)
    registration_form.fill_picture(picture_path)
    registration_form.fill_address(address)
    registration_form.fill_state(state)
    registration_form.fill_city(city)
    registration_form.submit()

    registration_form.assert_filled_full_name(firstName, lastName)
    registration_form.assert_filled_email(email)
    registration_form.assert_filled_gender(gender)
    registration_form.assert_filled_mobile(mobile)
    registration_form.assert_filled_birthday(birth_day, birth_month, birth_year)
    registration_form.assert_filled_subjects(subject1, subject2)
    registration_form.assert_filled_hobby(hobby)
    registration_form.assert_filled_picture(picture)
    registration_form.assert_filled_address(address)
    registration_form.assert_filled_state_and_city(state, city)
