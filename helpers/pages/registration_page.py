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

    def fill_picture(self, path):
        browser.element('#uploadPicture').send_keys(path)

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

    def should_registered_user_with(self, firstName, lastName, email, gender, mobile, birth_day, birth_month, birth_year,
                               subject1, subject2, hobby, picture, address, state, city):
        browser.all('tr').element_by(have.text('Student Name')).should(have.text(f'{firstName} {lastName}'))
        browser.all('tr').element_by(have.text('Student Email')).should(have.text(email))
        browser.all('tr').element_by(have.text('Gender')).should(have.text(gender))
        browser.all('tr').element_by(have.text('Mobile')).should(have.text(mobile))
        browser.all('tr').element_by(have.text('Date of Birth')).should(
            have.text(f'{birth_day} {birth_month},{birth_year}'))
        browser.all('tr').element_by(have.text('Subjects')).should(have.text(f'{subject1}, {subject2}'))
        browser.all('tr').element_by(have.text('Hobbies')).should(have.text(hobby))
        browser.all('tr').element_by(have.text('Picture')).should(have.text(picture))
        browser.all('tr').element_by(have.text('Address')).should(have.text(address))
        browser.all('tr').element_by(have.text('State and City')).should(have.text(f'{state} {city}'))


