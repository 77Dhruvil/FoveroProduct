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
    Detail_History_Leaves = (By.XPATH,'//*[@id="cell-1-18116"]/div/a')

    def get_sidebar_menu_HRMS(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Sidebar_menu_HRMS))

    def get_Leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Leaves))

    def get_upcomming_leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Upcomming_Leaves))



    def is_upcoming_leaves_present(self):
        try:
            # Wait and check if "No records" message is visible
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(HRMS.No_upcoming_leaves)
            )
            print("❌ No records found in Upcoming leaves")
            return False

        except TimeoutException:
            print("✅ Records are present in Upcoming leaves")
            return True
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
        return WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(HRMS.Detail_History_Leaves))


    def get_HRMS(self):
        self.get_sidebar_menu_HRMS().click()
        self.get_Leaves().click()
        self.get_upcomming_leaves().click()
        self.get_history_leaves().click()
        self.get_Detail_history_Leaves().click()

