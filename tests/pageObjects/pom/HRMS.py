import time

import pytest
import allure
from selenium.common import StaleElementReferenceException, TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HRMS:

    def __init__(self, driver):
        self.driver = driver

    # page locators
    Sidebar_menu_HRMS = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div/div[2]/a')
    Leaves = (By.CSS_SELECTOR,
              "#root > div.sc-cVzyXs.ieCMrL.sidebarOpen > div.rightSide > div > div > div > div.mb-5.custom-padding.col-lg-4.col-md-3.col-sm-12 > div > div:nth-child(2) > div:nth-child(1) > a > button")
    Upcomming_Leaves = (By.XPATH, '//*[@id="leaveList-tabpane-upcoming"]/div/div/div/div')
    No_upcoming_leaves = (By.XPATH, '//*[@id="leaveList-tabpane-upcoming"]/div/div/div/div/div')
    History_Leaves = (By.ID, 'leaveList-tab-history')
    Data_History_leaves = (By.XPATH, '//*[@id="cell-1-18116"]/div/a')
    Detail_History_Leaves = (By.XPATH, '//*[@id="cell-1-18116"]/div/a')
    Back_Button_Detail_History_leaves = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[1]/div[1]/div/a')
    Verify_casual_leaves = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[2]/div[2]/div/div[2]/ul[1]/li')
    Verify_Total_leaves = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[2]/div[2]/div/div[2]/ul[2]/li')
    Apply_leave_button = (By.XPATH,'/html/body/div/div[2]/div[3]/div[1]/div[2]')
    Leave_type_Dropdown = (By.XPATH,'//*[@id="leave_type"]/div/div[1]/div[2]')
    To_Dropdown = (By.XPATH,'//*[@id="to"]/div[1]')
    Start_From_date_field = (By.NAME,"start_date")




    def get_sidebar_menu_HRMS(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Sidebar_menu_HRMS))

    def get_Leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Leaves))

    def get_upcomming_leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Upcomming_Leaves))



    def is_no_records_message_displayed(self):

        try:
            element = self.driver.find_element(self.Upcomming_Leaves)
            return element.is_displayed() and element.text.strip() == "There are no records to display"
        except:
            return False

    def get_history_leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.History_Leaves))

    def get_data_history_leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Data_History_leaves))

    def is_history_leaves_present(self):
        try:
            # Wait and check if "No records" message is visible
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(HRMS.Data_History_leaves)
            )
            print("✅ Records are present in history Leaves")
            return True
        except TimeoutException:
            print("❌ No records found in history Leaves")
            return False

    def get_Detail_history_Leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Detail_History_Leaves))

    def get_Back_Button_Detail_History_Leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Back_Button_Detail_History_leaves))


    def get_Verify_casual_leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.Verify_casual_leaves))

    def get_Verify_total_leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.Verify_Total_leaves))

    def get_Apply_leave_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.Apply_leave_button))

    def get_Leave_type_Dropdown(self, leave_type="Casual Leave"):
        wait = WebDriverWait(self.driver, 10)

        # Open the dropdown
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="leave_type"]/div/div[1]/div[2]')))
        dropdown.click()

        # Select desired leave type
        option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{leave_type}')]")))
        option.click()

    def get_To_Dropdownn(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.To_Dropdown))

    def get_To_Dropdown(self,driver, user_list):
        wait = WebDriverWait(self.driver, 10)

        for user in user_list:

        # Open the dropdown
         dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="to"]/div[1]')))
         dropdown.click()

        # Select desired leave type
         user_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{user}']")))
         user_option.click()

    def get_start_from_date_field(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.Start_From_date_field))


    def get_select_date_picker(self , year, month, day):

        wait = WebDriverWait(self.driver, 10)

        # 1. Click on the "From" date field to open the date picker
        date_field = wait.until(EC.element_to_be_clickable((By.NAME,"start_date")))
        date_field.click()

        # 2. Select the year
        year_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/div/div/form/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select')))
        year_dropdown.click()

        year_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/div/div/form/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[126]')))
        year_option.click()

        # 3. Select the month
        month_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/div/div/form/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select')))
        month_dropdown.click()
        month_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/div/div/form/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[4]')))
        month_option.click()
        time.sleep(5)
        day_cell = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/div/div/form/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]')))
        day_cell.click()
        time.sleep(10)



    def get_HRMS(self):
        self.get_sidebar_menu_HRMS().click()
        self.get_Leaves().click()
        self.get_upcomming_leaves().click()
        self.get_history_leaves().click()
        print("Data displayed")
        self.get_Detail_history_Leaves().click()
        print("Detail displayed")
        self.get_Back_Button_Detail_History_Leaves().click()
        self.get_Verify_casual_leaves().click()
        self.get_Verify_total_leaves().click()
        print("Leaves value checked")
        self.get_Apply_leave_button().click()
        self.get_Leave_type_Dropdown()
        time.sleep(5)
        self.get_To_Dropdown(driver=self.driver, user_list=['Manish Patel', 'Tejas Patel'])
        time.sleep(5)
        self.get_start_from_date_field().click()
        self.get_select_date_picker('2025', '4','10')
