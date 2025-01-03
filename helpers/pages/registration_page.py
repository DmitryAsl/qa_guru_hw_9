import os
from selene import browser, be, have, command


class RegistrationPage:

    def __init__(self):
        self.subjectsInput = browser.element('#subjectsInput')

    def open(self):
        browser.open('/automation-practice-form')

    def fill_firstName(self, value):
        browser.element('#firstName').type(value)

    def fill_lastName(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_gender(self, gender):
        browser.element(f'input[value={gender}]').perform(command.js.click)

    def fill_mobile(self, mobile):
        browser.element('#userNumber').type(mobile)

    def fill_birthday(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.all('.react-datepicker__year-select option').element_by(have.text(year)).click()
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(have.text(month)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, subject1, *args):
        self.subjectsInput.click().type(subject1)
        browser.all('.subjects-auto-complete__menu').element_by(have.text(subject1)).click()
        for subject in args:
            self.subjectsInput.click().type(subject).press_enter()

    def fill_hobbby(self, hobby):
        browser.all('.custom-checkbox label').element_by(have.text(hobby)).click()

    def fill_picture(self, name):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'data', name))
        browser.element('#uploadPicture').send_keys(full_path)

    def submit(self):
        browser.element("#submit").click()

    def fill_address(self, address):
        browser.element('#currentAddress').type(address)

    def fill_state(self, state):
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.text(state)).click()

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.text(city)).click()

    def assert_filled_state_and_city(self, state, city):
        browser.all('tr').element_by(have.text('State and City')).should(have.text(f'{state} {city}'))

    def assert_filled_address(self, address):
        browser.all('tr').element_by(have.text('Address')).should(have.text(address))

    def assert_filled_picture(self, picture):
        browser.all('tr').element_by(have.text('Picture')).should(have.text(picture))

    def assert_filled_hobby(self, hobby):
        browser.all('tr').element_by(have.text('Hobbies')).should(have.text(hobby))

    def assert_filled_subjects(self, subject1, subject2):
        browser.all('tr').element_by(have.text('Subjects')).should(have.text(f'{subject1}, {subject2}'))

    def assert_filled_birthday(self, birth_day, birth_month, birth_year):
        browser.all('tr').element_by(have.text('Date of Birth')).should(
            have.text(f'{birth_day} {birth_month},{birth_year}'))

    def assert_filled_mobile(self, mobile):
        browser.all('tr').element_by(have.text('Mobile')).should(have.text(mobile))

    def assert_filled_gender(self, gender):
        browser.all('tr').element_by(have.text('Gender')).should(have.text(gender))

    def assert_filled_email(self, email):
        browser.all('tr').element_by(have.text('Student Email')).should(have.text(email))

    def assert_filled_full_name(self, firstname, lastname):
        browser.all('tr').element_by(have.text('Student Name')).should(have.text(f'{firstname} {lastname}'))
