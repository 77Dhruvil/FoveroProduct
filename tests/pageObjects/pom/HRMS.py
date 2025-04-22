import time

import pytest
import allure
from selenium.common import StaleElementReferenceException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HRMS:

    def __init__(self,driver):
        self.driver = driver


    # page locators
    Sidebar_menu_HRMS = (By.XPATH,'//*[@id="root"]/div[2]/div[2]/div/div/div[2]/a')
    Leaves = (By.CSS_SELECTOR,"#root > div.sc-cVzyXs.ieCMrL.sidebarOpen > div.rightSide > div > div > div > div.mb-5.custom-padding.col-lg-4.col-md-3.col-sm-12 > div > div:nth-child(2) > div:nth-child(1) > a > button")
    Upcomming_Leaves = (By.XPATH,'//*[@id="leaveList-tabpane-upcoming"]/div/div/div/div')





    def get_sidebar_menu_HRMS(self):
        return WebDriverWait (self.driver, timeout= 10).until(EC.presence_of_element_located(HRMS.Sidebar_menu_HRMS))

    def get_Leaves(self):
        return WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(HRMS.Leaves))

    def get_upcomming_leaves(self):
        return WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(HRMS.Upcomming_Leaves))

    def get_HRMS(self):
        self.get_sidebar_menu_HRMS().click()
        self.get_Leaves().click()
        self.get_upcomming_leaves().click()
        print("dsf sfdfsd f")
