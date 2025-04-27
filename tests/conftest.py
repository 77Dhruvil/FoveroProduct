import pytest
from selenium import webdriver

from tests.pageObjects.pom.loginpage import LoginPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://fovero.app/signin")
    loginpage = LoginPage(driver)
    loginpage.get_Fovero_Login(eml="dhruvil.patel@concettolabs.com", pwd="Devil@123")
    yield driver
    driver.quit()