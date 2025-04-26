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
    Project_name_click = (By.XPATH,'//*[@id="cell-1-754"]/div/a')
    project_name_estimation_tab = (By.ID,"project_details-tab-estimation")
    Estimation_Department_click = (By.XPATH,'//*[@id="cell-1-undefined"]/div')
    View_Estimation_popup_close = (By.CSS_SELECTOR,"body > div.modal.show > div > div > div > div.py-2.modal-header > button")
    Document_tab_click = (By.XPATH,'//*[@id="project_details"]/li[3]')
    Edit_project_Back_button = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/form/div[1]/div[2]')
    Search_bar = (By.ID,"search")
    Filter_Button = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[2]/div/div[1]/div[2]/img')
    Filter_Search_Button = (By.CSS_SELECTOR,"body > div.filterOffcanvas.offcanvas.offcanvas-end.show > div.offcanvas-body > div.w-auto.mt-3.col-lg-6.col-sm-12 > button.btn.btn-primary")
    Filter_Reset_Button = (By.CSS_SELECTOR,"body > div.filterOffcanvas.offcanvas.offcanvas-end.show > div.offcanvas-body > div.w-auto.mt-3.col-lg-6.col-sm-12 > button.btn.btn-secondary")
    Progressbar_click = (By.XPATH,'//*[@id="cell-5-754"]/div/div')
    Progressbar_Detail_page_Date_picker = (By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/div/div')
    Progressbar_Detail_page_Date_picker_start_date = (By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[6]')
    Progressbar_Detail_page_Date_picker_End_date = (By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[5]/div[7]')
    Progressbar_Detail_page_Close_button = (By.XPATH,'/html/body/div[2]/div[1]/button')
    def get_sidebar_menu_projects(self):
        return WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(Projects.Sidebar_Menu_Projects))

    def get_project_name_click(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Project_name_click))

    def get_project_Estimation_tab(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.project_name_estimation_tab))

    def get_Estimation_Department_click(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Estimation_Department_click))

    def get_view_estimation_popup_close(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.View_Estimation_popup_close))

    def get_Document_tab_click(self):
        add_project_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="project_details"]/li[3]'))
        )
        add_project_button.click()

    def get_edit_project_back_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Edit_project_Back_button))

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

    def get_filter_reset_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Filter_Reset_Button))

    def get_progressbar_click(self):
        return WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located(Projects.Progressbar_click)
        )

    def get_progressbar_Detail_page_Date_picker(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Progressbar_Detail_page_Date_picker)
        )

    def get_progressbar_Detail_page_Date_picker_start_date(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Progressbar_Detail_page_Date_picker_start_date)
        )

    def get_progressbar_Detail_page_Date_picker_end_date(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Progressbar_Detail_page_Date_picker_End_date)
        )

    def get_progressbar_Detail_page_Close_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Progressbar_Detail_page_Close_button)
        )


    def get_Projects(self):

        try:
            self.get_sidebar_menu_projects().click()
        except TimeoutException:
            pytest.fail("Sidebar menu for Projects did not load in time")


        try:
            self.get_project_name_click().click()
        except TimeoutException:
            pytest.fail("Project name is not clickable or not loaded at a time")

        try:
            self.get_project_Estimation_tab().click()
        except TimeoutException:
            pytest.fail("Project Estimation tab is not clickable or not loaded at a time")

        try:
            self.get_Estimation_Department_click().click()
        except TimeoutException:
            pytest.fail("Project Estimation Department click is not clickable or not loaded at a time")

        try:
            self.get_view_estimation_popup_close().click()
        except TimeoutException:
            pytest.fail("Project Estimation Pop up click is not clickable or not loaded at a time")

        try:
            self.get_Document_tab_click()
        except TimeoutException:
            pytest.fail("Project Document tab  click is not clickable or not loaded at a time")

        try:
            self.get_edit_project_back_button().click()
        except TimeoutException:
            pytest.fail("Project Edit button  click is not clickable or not loaded at a time")

        time.sleep(2)

        try:
            self.get_search_bar().send_keys("ECO Solution")
        except TimeoutException:
            pytest.fail("Search bar  click is not clickable or not working")

        try:
            self.get_search_bar().clear()
        except TimeoutException:
            pytest.fail("Search bar  value is not cleared from the search bar")

        try:
            self.get_Filter_button().click()
        except TimeoutException:
            pytest.fail("Filter button is not clickable or filter menu is not opened")

        try:
            self.get_status_filter_Drpdwn()
        except TimeoutException:
            pytest.fail("Status filter dropdown is not clickable or opended")


        keyboard.write("Archived")

        keyboard.press("enter")

        try:
            self.get_status_filter_Drpdwn()
        except TimeoutException:
            pytest.fail("To close the sidebar menu")

        try:
            self.get_filter_search_button().click()
        except TimeoutException:
            pytest.fail("Filter button is not clickable ")

        try:
            self.get_Filter_button().click()
        except TimeoutException:
            pytest.fail("Again filter sidebar menu is not opened ")

        time.sleep(5)

        try:
            self.get_filter_reset_button().click()
        except TimeoutException:
            pytest.fail("Filter reset button is not clickable ")

        time.sleep(5)

        try:
            self.get_progressbar_click().click()
        except TimeoutException:
            pytest.fail("progressbar is not clickable ")

        time.sleep(5)

        try:
            self.get_progressbar_Detail_page_Date_picker().click()
        except TimeoutException:
            pytest.fail("Date picker is not clickable ")

        try:
            self.get_progressbar_Detail_page_Date_picker_start_date().click()
        except TimeoutException:
            pytest.fail("Start date is not clickable ")


        try:
            self.get_progressbar_Detail_page_Date_picker_end_date().click()
        except TimeoutException:
            pytest.fail("End date is not clickable ")

        try:
            self.get_progressbar_Detail_page_Close_button().click()
        except TimeoutException:
            pytest.fail("Progressbar Detial page is not closed ")




