import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.config.hold_browser_open = True
    browser.open('https://duckduckgo.com')

