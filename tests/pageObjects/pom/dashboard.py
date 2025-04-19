import time
from lib2to3.pgen2 import driver
import pyautogui
import self

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    Weekly_recorded_hrs_viewall = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div/a')
    punch_in_out_back_button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[1]/div/a')
    sidebar_menu_dashboard = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div[1]/a')
    Todays_birthday = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/button[1]')
    Upcoming_birthday = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/button[2]')
    Recent_Timesheet = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[1]/a')
    Close_Recent_Timesheet = (By.XPATH, '/html/body/div[3]/div/div/div/div[1]/button')
    view_Recent_Timesheet = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div[5]/img')
    close_Report_Timesheet = (By.XPATH,'/html/body/div[3]/div/div/div/div[1]/button')
    Apply_Leave_button = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[4]/div/div/div[1]/div[2]/a')
    Back_Apply_Leave_Button = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[1]/div/a')



    def get_user_weekly_recorded_hrs_viewall(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.Weekly_recorded_hrs_viewall)
        )

    def get_punch_in_out_back_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.punch_in_out_back_button)
        )

    def get_sidebar_menu_back_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.sidebar_menu_dashboard)
        )

    def get_Todays_birthday(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.Todays_birthday)
        )

    def get_Upcoming_birthday(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.Upcoming_birthday)
        )

    def get_Recent_Timesheet(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.Recent_Timesheet)
        )

    def get_close_Recent_Timesheet(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.Close_Recent_Timesheet)
        )
    def get_View_Recent_Timesheet(self):
        return WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located(Dashboard.view_Recent_Timesheet)
        )

    def get_Close_Report_Timesheet(self):
        return WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located(Dashboard.Close_Recent_Timesheet)
        )

    def get_Apply_Leave_Button(self):
        return WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located(Dashboard.Apply_Leave_button)
        )
    def get_Back_Apply_Leave_Button(self):
        return WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located(Dashboard.Back_Apply_Leave_Button)
        )

    def check_birthday_section(self, tab_name="Today's"):
        if tab_name == "Today's":
            self.get_Todays_birthday().click()
        elif tab_name == "Upcoming":
            self.get_Upcoming_birthday().click()
        else:
            print("❌ Invalid tab name.")
            return []

        time.sleep(2)
        birthday_elements = self.driver.find_elements(By.XPATH,
                                                      '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[2]')
        if birthday_elements:
            result = []
            for element in birthday_elements:
                print(f"{tab_name} Birthday Info ➤ {element.text}")
                result.append(element.text)
                return result


        else:
            print(f"{tab_name} ➤ No birthday data found.")
            pass



    def get_Fovero_Dashboard(self):
        self.get_user_weekly_recorded_hrs_viewall().click()

        self.get_punch_in_out_back_button().click()

        self.get_sidebar_menu_back_button().click()

        pyautogui.scroll(-500)  # Scrolls down
        self.get_Recent_Timesheet().click()

        print("abc")
        self.get_close_Recent_Timesheet().click()
        self.get_View_Recent_Timesheet().click()
        self.get_Close_Report_Timesheet().click()
        self.get_Apply_Leave_Button().click()
        self.get_Back_Apply_Leave_Button().click()
        self.get_sidebar_menu_back_button().click()
        print("Completed")







        # self.get_Todays_birthday().click()
        # time.sleep(5)
        # self.get_Upcoming_birthday().click()

