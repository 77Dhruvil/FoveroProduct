import time

from selenium.webdriver.common.by import By

class Dashboard:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    Weekly_recorded_hrs_viewall = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div/a')
    punch_in_out_back_button = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[1]/div/a')
    sidebar_menu_dashboard = (By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/div/div[1]/a')
    Todays_birthday = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/button[1]')
    Upcoming_birthday = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/button[2]')




    def get_user_weekly_recorded_hrs_viewall(self):
        return self.driver.find_element(*Dashboard.Weekly_recorded_hrs_viewall)

    def get_punch_in_out_back_button(self):
        return self.driver.find_element(*Dashboard.punch_in_out_back_button)

    def get_sidebar_menu_back_button(self):
        return self.driver.find_element(*Dashboard.sidebar_menu_dashboard)

    def get_Todays_birthday(self):
        return self.driver.find_element(*Dashboard.Todays_birthday)

    def get_Upcoming_birthday(self):
        return self.driver.find_element(*Dashboard.Upcoming_birthday)

    def get_Fovero_Dashboard(self):
        self.get_user_weekly_recorded_hrs_viewall().click()
        time.sleep(5)
        self.get_punch_in_out_back_button().click()
        time.sleep(5)
        self.get_sidebar_menu_back_button().click()
        time.sleep(5)
        self.get_Todays_birthday().click()
        time.sleep(5)
        self.get_Upcoming_birthday().click()