import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def browser_size():
    browser.open('https://google.com')
    browser.driver.set_window_size(1024,680)


def test_google_search_ok(browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_fail(browser_size):
    browser.element('[name="q"]').should(be.blank).set_value('sdfosdfsdkfljkd').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
