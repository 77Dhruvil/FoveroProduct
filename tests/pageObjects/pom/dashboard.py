import time
import allure
from lib2to3.pgen2 import driver
import pyautogui
import pytest
from selenium.common import TimeoutException, NoSuchElementException

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
    Todays_birthday_Forward_button = ( By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/button[2]')
    Todays_birthday_Backward_button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/button[1]')
    Upcoming_birthday = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[1]/div/div/button[2]')
    Upcoming_birthday_Forward_button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/button[2]')
    Upcoming_birthday_Backward_button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/button[1]')
    Recent_Timesheet = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[1]/a')
    Close_Recent_Timesheet = (By.XPATH, '/html/body/div[3]/div/div/div/div[1]/button')
    view_Recent_Timesheet = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[3]/div/div/div[2]/div[2]/div/div/div[5]/img')
    close_Report_Timesheet = (By.XPATH, '/html/body/div[3]/div/div/div/div[1]/button')
    Apply_Leave_button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div[4]/div/div/div[1]/div[2]/a')
    Back_Apply_Leave_Button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[1]/div/a')
    Go_To_Dashboard = (By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/div/div[1]/a')



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

    def get_Todays_birthday_Forward_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.Todays_birthday_Forward_button)
        )

    def get_Todays_Birthday_Backward_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.Todays_birthday_Backward_button)
        )

    def get_Upcoming_birthday(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Dashboard.Upcoming_birthday)
        )

    def get_Upcoming_Birthday_Forward_Button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.Upcoming_birthday_Forward_button)
        )

    def get_Upcoming_Birthday_Backward_Button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.Upcoming_birthday_Backward_button)
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
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.view_Recent_Timesheet)
        )

    def get_Close_Report_Timesheet(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.Close_Recent_Timesheet)
        )

    def get_Apply_Leave_Button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.Apply_Leave_button)
        )

    def get_Back_Apply_Leave_Button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Dashboard.Back_Apply_Leave_Button)

        )

    def get_go_to_Dashboard(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(Dashboard.Go_To_Dashboard))




    def check_birthday_section(self, tab_name="Today's"):
        if tab_name == "Today's":
            self.get_Todays_birthday().click()
            time.sleep(1)

            # Forward click if visible and enabled
            try:
                btn = self.get_Todays_birthday_Forward_button()
                if btn.is_displayed() and btn.is_enabled():
                    btn.click()
                    time.sleep(1)
            except Exception:
                print("Forward button not available or clickable.")

            # Backward click if visible and enabled
            try:
                btn = self.get_Todays_Birthday_Backward_button()
                if btn.is_displayed() and btn.is_enabled():
                    btn.click()
            except Exception:
                print("Backward button not available or clickable.")

        elif tab_name == "Upcoming":
            self.get_Upcoming_birthday().click()
            time.sleep(1)

            try:
                btn = self.get_Upcoming_Birthday_Forward_Button()
                if btn.is_displayed() and btn.is_enabled():
                    btn.click()
                    time.sleep(1)
            except Exception:
                print("Upcoming Forward button not available.")

            try:
                btn = self.get_Upcoming_Birthday_Backward_Button()
                if btn.is_displayed() and btn.is_enabled():
                    btn.click()
            except Exception:
                print("Upcoming Backward button not available.")

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

    @allure.step("Click on 'View All' in Weekly Recorded Hours")
    def fovero_dashboardd(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.Weekly_recorded_hrs_viewall))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="ViewAll_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("View all button is not clickable") from e

    @allure.step("Click on 'Punch in/out Back button")
    def punch_inn_out_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.punch_in_out_back_button))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="PunchInOut_BackBtn_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("Back button is not clickable") from e

    @allure.step("Click on sidebar menu back button")

    def sidebar_menu_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.sidebar_menu_dashboard))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Sidebarmenu_BackBtn_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("sidebar Back button is not clickable") from e

    pyautogui.scroll(-500)  # Scrolls down

    @allure.step("Click on Recent timesheet")
    def recent_timesheet(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.Recent_Timesheet))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Recent_Time_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("Recent timesheet button is not clickable") from e

    @allure.step("Click on close button to  Recent timesheet")
    def close_recent_timesheet(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.Close_Recent_Timesheet))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Close_button_Recent_timesheet_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("close recent timesheet button is not clickable") from e

    pyautogui.scroll(-500)
    @allure.step("Click on View  Recent timesheet")
    def view_recent_timesheet(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.view_Recent_Timesheet))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="View_timesheet_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("View Recent timesheet button is not clickable") from e

    @allure.step("Close Report timesheet")
    def close_report_timesheet(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.close_Report_Timesheet))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Close_Report_timesheet_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("close report timesheet button is not clickable") from e

    pyautogui.scroll(-500)
    @allure.step("Apply leave button")
    def apply_leave_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.Apply_Leave_button))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Apply_leave_button_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("Apply leave button is not clickable") from e

    @allure.step("Apply leave Back button")
    def apply_leave_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.Back_Apply_Leave_Button))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Apply_leave_Back_button_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("Apply leave Back button is not clickable") from e

    @allure.step("Side bar menu dashboard Back button")
    def sidebarr_menu_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.sidebar_menu_dashboard))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Sidebar_menu_dashboard_back_button_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("sidebar menu back button is not clickable") from e

    @allure.step("Go to Dashboard ")
    def go_to_dashboard(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Dashboard.Go_To_Dashboard))
        except TimeoutException as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Go_To_Dashboard_button_Error",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception("Go to dashbord menu click is not working") from e





