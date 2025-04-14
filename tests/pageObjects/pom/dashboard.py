from selenium.webdriver.common.by import By

class Dashboard:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    user_loggedin = (By.XPATH,"/html/body/div/div[2]/div[1]/div[1]/div[2]/div[4]/button/span")

    def get_user_loggedin(self):
        return self.driver.find_element(*Dashboard.user_loggedin)

