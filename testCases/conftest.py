from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop('Plugins', None)

