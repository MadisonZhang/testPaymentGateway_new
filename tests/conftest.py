import pytest
from selenium import webdriver

@pytest.fixture(scope='module')
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()