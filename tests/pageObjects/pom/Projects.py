import time
import keyboard

import pytest
import allure
from selenium.common import StaleElementReferenceException, TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Projects:

    def __init__(self, driver):
        self.driver = driver



    #Page Locators
    Sidebar_Menu_Projects = (By.CSS_SELECTOR,"#root > div.sc-cVzyXs.ieCMrL.sidebarOpen > div.sc-YysOf.eZhCtH.scrollbar.sidebar > div > div > div:nth-child(3) > a")
    Search_bar = (By.ID,"search")
    Filter_Button = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[2]/div/div[1]/div[2]/img')
    Filter_Search_Button = (By.CSS_SELECTOR,"body > div.filterOffcanvas.offcanvas.offcanvas-end.show > div.offcanvas-body > div.w-auto.mt-3.col-lg-6.col-sm-12 > button.btn.btn-primary")


    def get_sidebar_menu_projects(self):
        return WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(Projects.Sidebar_Menu_Projects))

    def get_search_bar(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Search_bar))

    def get_Filter_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Filter_Button))

    def get_status_filter_Drpdwn(self):
        wait = WebDriverWait(self.driver, 10)

        # 1. Click on the Status field to open the Status dropdown
        status_drp_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status"]/div[1]')))
        status_drp_field.click()

    def get_filter_search_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Filter_Search_Button))


    def get_Projects(self):
        self.get_sidebar_menu_projects().click()
        time.sleep(5)
        self.get_search_bar().send_keys("Fovero")
        time.sleep(2)
        self.get_search_bar().clear()
        time.sleep(10)
        self.get_Filter_button().click()
        time.sleep(5)
        self.get_status_filter_Drpdwn()
        time.sleep(5)
        keyboard.write("Archived")
        time.sleep(5)
        keyboard.press("enter")
        time.sleep(5)
        self.get_status_filter_Drpdwn()
        time.sleep(5)
        self.get_filter_search_button().click()
        time.sleep(5)




