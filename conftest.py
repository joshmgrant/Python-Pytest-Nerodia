import pytest
from _pytest.runner import runtestprotocol
from nerodia.browser import Browser
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from os import environ


def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            print('\n%s --- %s' % (item.name, report.outcome))
    return True

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
    caps['name'] = request.node.name
    caps['buildTag'] = build_tag

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    remote = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=caps
    )

    browser = Browser(browser=remote, desired_capabilities=caps)
    yield browser
    browser.quit()