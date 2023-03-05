import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_width = 1068
    browser.config.window_height = 1440
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True
