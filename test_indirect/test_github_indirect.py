import pytest
from selene import browser, by


@pytest.mark.parametrize("desktop_version", [(1650, 1050)], indirect=True)
def test_desktop(desktop_version):
    browser.open("http://github.com")
    browser.element(by.text("Sign up")).click()


@pytest.mark.parametrize("mobile_version", [(900, 1000)], indirect=True)
def test_mobile(mobile_version):
    browser.open("http://github.com")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()
