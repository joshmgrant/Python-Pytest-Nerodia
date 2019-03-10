import pytest
from nerodia.browser import Browser
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from os import environ


@pytest.fixture
def browser(request):
    caps = {
        "platform": "Windows 10",
        "browserName": "firefox",
        "version": "59.0"
    }

    build_tag = "nerodia-build"
    username = environ.get('SAUCE_USERNAME', None)
    access_key = environ.get('SAUCE_ACCESS_KEY', None)

    selenium_endpoint = "http://ondemand.saucelabs.com/wd/hub"
    
    caps['username'] = username
    caps['accesskey'] = access_key
    caps['name'] = 'nerodia_test'
    caps['buildTag'] = build_tag

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    remote = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=caps
    )

    browser = Browser(browser=remote, desired_capabilities=caps)
    yield browser
    browser.quit()