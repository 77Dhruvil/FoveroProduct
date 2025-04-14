from selenium.webdriver.common.by import By
from tests.utils.common_utils import webdriver_wait

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    Email = (By.ID, "email")
    Password = (By.ID, "password")
    Sigin_button = (By.CSS_SELECTOR, "#root > div.sc-fMMURN.lpljxX.bg-grey-lighter.d-flex.align-items-center > div > div > div.col-xl-6.col-lg-8.offset-xl-0.offset-lg-2 > div > div > form > div:nth-child(2) > div > button")
  #  Forgot_password = (By.CSS_SELECTOR, "#root > div.sc-fMMURN.lpljxX.bg-grey-lighter.d-flex.align-items-center > div > div > div.col-xl-6.col-lg-8.offset-xl-0.offset-lg-2 > div > div > form > div:nth-child(3) > div > a")
    Many_attemps_error = (By.XPATH,"/html/body/div/div[1]/div/div/button")
    Error_message = (By.CSS_SELECTOR, "#\31  > div.Toastify__toast-body")

    #Page Actions
    def get_EMail(self):
        return self.driver.find_element(*LoginPage.Email)
    def get_Password(self):
        return self.driver.find_element(*LoginPage.Password)

    def get_Sign_button(self):
        return self.driver.find_element(*LoginPage.Sigin_button)
    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.Email)
        return self.driver.find_element(*LoginPage.Error_message)

    def get_Fovero_Login(self, eml , pwd ):
        self.get_EMail().send_keys(eml)
        self.get_Password().send_keys(pwd)
        self.get_Sign_button().click()

    def get_error_message(self):
      return  self.get_error_message().text

