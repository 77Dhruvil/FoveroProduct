import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://fovero.app/signin")
    yield driver
    driver.quit()