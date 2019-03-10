import pytest
from _pytest.runner import runtestprotocol
from nerodia.browser import Browser
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from os import environ


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Needed pytest hook for accessing pass/fail results
    in the pytest fixture here.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


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
    caps['build'] = build_tag

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    remote = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=caps
    )

    browser = Browser(browser=remote, desired_capabilities=caps)
    yield browser
    
    sauce_result = "failed" if request.node.rep_call.failed else "passed"
    browser.execute_script("sauce:job-result={}".format(sauce_result))
    browser.quit()