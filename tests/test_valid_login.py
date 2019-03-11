import pytest


def test_standard_user(browser):
    browser.goto('http://www.saucedemo.com')

    browser.text_field(data_test='username').value = 'standard_user'
    browser.text_field(data_test='password').value ='secret_sauce'
    browser.button(type='submit').click()

    assert "/inventory.html" in browser.url
    