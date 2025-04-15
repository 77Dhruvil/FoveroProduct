import time
import allure
import pytest
from selenium import webdriver
from tests.pageObjects.pom.loginpage import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://fovero.app/signin")
    yield driver
    driver.quit()


# @allure.epic("Fovero Login Test")
# @allure.feature("TC#1 - Fovero Login Negative Test")
# @pytest.mark.negative

# def test_FoveroLogin_Negative(setup):

#         loginpage = LoginPage(driver=setup)
#         loginpage.get_Fovero_Login(eml="dhruvil.patel@concettolabs.com", pwd="Devil@1234")
#         time.sleep(2)
       #  webdriver_wait(setup, By.CSS_SELECTOR, "#\31  > div.Toastify__toast-body(), 'Incorrect username or password.')]")
#
#         error_msg_element = loginpage.get_error_message()
#         assert error_msg_element == "Incorrect username or password."

@allure.epic("Fovero Login Test")
@allure.feature("TC#2 - Fovero Login Positive Test")
@pytest.mark.positive
def test_FoveroLogin_Positive(driver):
    loginpage = LoginPage(driver)
    loginpage.get_Fovero_Login(eml="dhruvil.patel@concettolabs.com", pwd="Devil@123")
    time.sleep(10)
