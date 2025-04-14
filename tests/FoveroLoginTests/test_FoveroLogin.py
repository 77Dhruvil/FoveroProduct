import  time
import  allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.pageObjects.pom.loginpage import LoginPage
from tests.pageObjects.pom.dashboard import Dashboard
from tests.utils.common_utils import webdriver_wait


# Assertions and will use the pageobject class

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://fovero.app/signin")
    return driver

@allure.epic("Fovero Login Test")
@allure.feature("TC#1 - Fovero Login Negative Test")
@pytest.mark.negative
def test_FoveroLogin_Negative(setup):
    #try:

        loginpage = LoginPage(driver=setup)
        loginpage.get_Fovero_Login(eml="dhruvil.patel@concettolabs.com", pwd="Devil@1234")
        time.sleep(2)
      #  webdriver_wait(setup, By.CSS_SELECTOR, "#\31  > div.Toastify__toast-body(), 'Incorrect username or password.')]")

        error_msg_element = loginpage.get_error_message()
        assert error_msg_element == "Incorrect username or password."

    # except Exception as  e:
    #     pytest.xfail("Failed TC")
    #     print(e)

@allure.epic("Fovero Login Test")
@allure.feature("TC#2 - Fovero Login Positive Test")
@pytest.mark.positive
def test_FoveroLogin_Positive(setup):
  #  try:
        loginpage = LoginPage(driver=setup)
        loginpage.get_Fovero_Login(eml="dhruvil.patel@concettolabs.com", pwd="Devil@123")
        time.sleep(10)
        dashboard = Dashboard(driver=setup)
        assert "Dhruvil Patel" in dashboard.user_loggedin()

    # except Exception as e:
    #     pytest.xfail("Failed TC")
    #     print(e)

