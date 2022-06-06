import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def set_up():
    driver = webdriver.Chrome('/Users/mihaillipkovskij/Downloads/chromedriver')
    driver.maximize_window()
    driver

    yield driver
    driver.quit()
