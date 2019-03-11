import pytest


def test_locked_out_user(browser):
    browser.goto('http://www.saucedemo.com')

    browser.text_field(data_test='username').value = 'locked_out_user'
    browser.text_field(data_test='password').value ='secret_sauce'
    browser.button(type='submit').click()

    assert browser.button(class_name='error-button').exists
    