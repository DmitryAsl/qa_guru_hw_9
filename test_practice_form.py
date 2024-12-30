import os
from selene import browser, be, have, command

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


def test_full_content_form():
    browser.open('/automation-practice-form')
    # заполнение всех полей формы
    browser.element('#firstName').type(firstName)
    browser.element('#lastName').type(lastName)
    browser.element('#userEmail').type(email)
    browser.element(f'input[value={gender}]').perform(command.js.click)
    browser.element('#userNumber').type(mobile)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select option').element_by(have.text(birth_year)).click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.text(birth_month)).click()
    browser.element(f'.react-datepicker__day--0{birth_day}').click()
    browser.element('#subjectsInput').click().type(subject1)
    browser.all('.subjects-auto-complete__menu').element_by(have.text(subject1)).click()
    browser.element('#subjectsInput').click().type(subject2).press_enter()
    browser.all('.custom-checkbox label').element_by(have.text(hobby)).click()
    browser.element('#uploadPicture').send_keys(picture_path)
    browser.element('#currentAddress').type(address)
    browser.element('#state').click()
    browser.all('[id^="react-select-3-option"]').element_by(have.text(state)).click()
    browser.element('#city').click()
    browser.all('[id^="react-select-4-option"]').element_by(have.text(city)).click()

    browser.element("#submit").click()

    # проверка таблицы заполненных полей
    # альтернативная проверка для полей - browser.element(f'//tr[td[1][text()="Mobile"]]/td[2][text()="{mobile}"]').should(be.visible)
    browser.all('tr').element_by(have.text('Student Name')).should(have.text(f'{firstName} {lastName}'))
    browser.all('tr').element_by(have.text('Student Email')).should(have.text(email))
    browser.all('tr').element_by(have.text('Gender')).should(have.text(gender))
    browser.all('tr').element_by(have.text('Mobile')).should(have.text(mobile))
    browser.all('tr').element_by(have.text('Date of Birth')).should(
        have.text(f'{birth_day} {birth_month},{birth_year}'))
    browser.all('tr').element_by(have.text('Subjects')).should(have.text(f'{subject1}, {subject2}'))
    browser.all('tr').element_by(have.text('Hobbies')).should(have.text(hobby))
    browser.all('tr').element_by(have.text('Picture')).should(have.text(picture))
    browser.all('tr').element_by(have.text('Hobbies')).should(have.text(hobby))
    browser.all('tr').element_by(have.text('Address')).should(have.text(address))
    browser.all('tr').element_by(have.text('State and City')).should(have.text(f'{state} {city}'))
