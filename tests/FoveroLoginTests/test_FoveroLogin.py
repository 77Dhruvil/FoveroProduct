import time
import allure
import pytest
from selenium import webdriver
from tests.pageObjects.pom.loginpage import LoginPage

@allure.epic("Fovero Login Test")
@allure.feature("TC#2 - Fovero Login Positive Test")
@pytest.mark.positive
def test_FoveroLogin_Positive(driver):
    loginpage = LoginPage(driver)
    loginpage.get_Fovero_Login(eml="dhruvil.patel@concettolabs.com", pwd="Devil@123")
    time.sleep(10)
