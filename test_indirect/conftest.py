import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080)])
def desktop_version(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(1000, 1080)])
def mobile_version(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()
