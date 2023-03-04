import pytest
from selene import browser, have, be

@pytest.fixture()
def browser_setup():
    browser.config.window_width = 768
    browser.config.window_height = 1440
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.hold_browser_open = True



def test_registration_form(browser_setup):
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Petrov')
    browser.element('#userEmail').type('petrov@abc.com')
    browser.element('#genterWrapper label').should(have.exact_text('Male')).click()
    browser.element('#userNumber').type('7123456789')
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()