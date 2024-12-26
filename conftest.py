import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(params=[(1920, 1080), (1000, 1080)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 1012:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()