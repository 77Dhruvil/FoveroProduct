import time

import keyboard

import pytest
import allure
from selenium.common import StaleElementReferenceException, TimeoutException, NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class Projects:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        # Scrolls the element into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    # Page Locators
    Sidebar_Menu_Projects = (By.CSS_SELECTOR,
                             "#root > div.sc-cVzyXs.ieCMrL.sidebarOpen > div.sc-YysOf.eZhCtH.scrollbar.sidebar > div > div > div:nth-child(3) > a")
    Project_name_click = (By.XPATH, '//*[@id="cell-1-754"]/div/a')
    project_name_estimation_tab = (By.ID, "project_details-tab-estimation")
    Estimation_Department_click = (By.XPATH, '//*[@id="cell-1-undefined"]/div')
    View_Estimation_popup_close = (
        By.CSS_SELECTOR, "body > div.modal.show > div > div > div > div.py-2.modal-header > button")
    Document_tab_click = (By.XPATH, '//*[@id="project_details"]/li[3]')
    Edit_project_Back_button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/form/div[1]/div[2]')
    Search_bar = (By.ID, "search")
    Filter_Button = (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/div[1]/div[2]/img')
    Filter_Search_Button = (By.CSS_SELECTOR,
                            "body > div.filterOffcanvas.offcanvas.offcanvas-end.show > div.offcanvas-body > div.w-auto.mt-3.col-lg-6.col-sm-12 > button.btn.btn-primary")
    Filter_Reset_Button = (By.CSS_SELECTOR,
                           "body > div.filterOffcanvas.offcanvas.offcanvas-end.show > div.offcanvas-body > div.w-auto.mt-3.col-lg-6.col-sm-12 > button.btn.btn-secondary")
    Progressbar_click = (By.XPATH, '//*[@id="cell-5-754"]/div/div')
    Progressbar_Detail_page_Date_picker = (By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div')
    Progressbar_Detail_page_Date_picker_start_date = (
        By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[6]')
    Progressbar_Detail_page_Date_picker_End_date = (
        By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[5]/div[7]')
    Progressbar_Detail_page_Close_button = (By.XPATH, '/html/body/div[2]/div[1]/button')

    def get_sidebar_menu_projects(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Sidebar_Menu_Projects))

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
        status_drp_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="status"]/div[1]/div[1]/div[2]')))
        status_drp_field.click()

    def get_filter_search_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Filter_Search_Button))

    def get_filter_reset_button(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(Projects.Filter_Reset_Button))

    def get_progressbar_click(self):
        return WebDriverWait(self.driver, timeout=10).until(
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

    def Sidebar_menu_project(self):

        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Sidebar_Menu_Projects))
        except TimeoutException as e:
            raise Exception("Sidebar menu for Projects did not load in time") from e

    def project_name_click(self):

        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Project_name_click))
        except TimeoutException as e:
            raise Exception("Project name is not clickable or not loaded at a time") from e

    def Project_Esitmation_tab(self):

        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.project_name_estimation_tab))
        except TimeoutException as e:
            raise Exception("Project Estimation tab is not clickable or not loaded at a time") from e

    def Estimation_department_click(self):

        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Estimation_Department_click))
        except TimeoutException as e:
            raise Exception("Project Estimation Department click is not clickable or not loaded at a time") from e

    def Estimation_view_popup_close(self):

        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.View_Estimation_popup_close))
        except TimeoutException as e:
            raise Exception("Project Estimation Pop up click is not clickable or not loaded at a time") from e

    def Document_tabb_click(self):

        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Document_tab_click))
        except TimeoutException as e:
            raise Exception("Project Document tab  click is not clickable or not loaded at a time") from e

    def Edit_project_back_button(self):
        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Edit_project_Back_button))
        except TimeoutException as e:
            raise Exception("Project Edit button  click is not clickable or not loaded at a time") from e

    time.sleep(2)

    def search_bar(self):
        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Search_bar))
        except TimeoutException as e:
            raise Exception("Search bar  value is not cleared from the search bar") from e

    def filter_button(self):

        try:

            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Filter_Button))
        except TimeoutException as e:
            raise Exception("Filter button is not clickable or filter menu is not opened") from e

    def filter_button_click(self):

        try:
            self.get_status_filter_Drpdwn()
        except TimeoutException:
            pytest.fail("Status filter dropdown is not clickable or opended")

        keyboard.write("Archived")

        keyboard.press("enter")

        try:
            self.get_status_filter_Drpdwn()
        except (TimeoutException, NoSuchElementException) as e:
            pytest.fail("To close the sidebar menu")

    def filterr_search_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Filter_Search_Button))
        except TimeoutException as e:
            raise Exception("Again filter sidebar menu is not opened") from e

    time.sleep(10)

    def Reset_button(self):
        try:
            # Wait until the reset button is visible
            reset_btn = WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Filter_Reset_Button)
            )

            # Wait for the button to be clickable and then click it
            WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(Projects.Filter_Reset_Button)
            )

            reset_btn.click()
            return None


        except StaleElementReferenceException:

            # In case the element became stale, try locating it again

            print("Element became stale, re-locating the element.")

            return self.Reset_button()  # Recursive call to re-locate and click again


        except TimeoutException as e:

            raise Exception("Reset Filter button not found or not clickable within the timeout") from e

        except Exception as e:

            raise Exception("An unexpected error occurred while interacting with the Reset Filter button.") from e

    time.sleep(10)

    def progress_button_click(self):
        try:
            # Wait for the progress button to be visible
            progress_btn = WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Progressbar_click)
            )

            # Wait for the element to be clickable
            WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(Projects.Progressbar_click)
            )

            progress_btn.click()
            return None


        except StaleElementReferenceException:

            # In case the element became stale, try locating it again

            print("Element became stale, re-locating the element.")

            return self.progress_button_click()  # Recursive call to re-locate and click again


        except TimeoutException as e:

            raise Exception("Progress button not found or not clickable within the timeout") from e

        except Exception as e:

            raise Exception("An unexpected error occurred while interacting with the Reset Filter button.") from e

    time.sleep(5)

    def Date_picker(self):
        try:
            # Wait for the progress button to be visible
            progress_btn_date_picker = WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Progressbar_Detail_page_Date_picker)
            )

            # Wait for the element to be clickable
            WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(Projects.Progressbar_Detail_page_Date_picker)
            )

            progress_btn_date_picker.click()
            return None


        except StaleElementReferenceException:

            # In case the element became stale, try locating it again

            print("Element became stale, re-locating the element.")

            return self.Date_picker()  # Recursive call to re-locate and click again


        except TimeoutException as e:

            raise Exception("Start date  not found or not clickable within the timeout") from e

        except Exception as e:

            raise Exception("An unexpected error occurred while interacting with the Reset Filter button.") from e

    time.sleep(5)

    def start_date_picker(self):

        try:
            progress_btn_start_date = WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Progressbar_Detail_page_Date_picker_start_date)
            )

            # Wait for the element to be clickable
            WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(Projects.Progressbar_Detail_page_Date_picker_start_date)
            )

            progress_btn_start_date.click()
            return None

        except StaleElementReferenceException:

            # In case the element became stale, try locating it again

            print("Element became stale, re-locating the element.")

            return self.start_date_picker()  # Recursive call to re-locate and click again

        except TimeoutException as e:

            raise Exception("Start date  not found or not clickable within the timeout") from e

        except Exception as e:

            raise Exception("An unexpected error occurred while interacting with the Reset Filter button.") from e


    def end_date_picker(self):
        try:
            progress_btn_end_date = WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Progressbar_Detail_page_Date_picker_End_date)
            )

        # Wait for the element to be clickable
            WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(Projects.Progressbar_Detail_page_Date_picker_End_date)
            )

            progress_btn_end_date.click()
            return None

        except StaleElementReferenceException:

# In case the element became stale, try locating it again

                print("Element became stale, re-locating the element.")

                return self.end_date_picker()  # Recursive call to re-locate and click again

        except TimeoutException as e:

                raise Exception("End date  not found or not clickable within the timeout") from e

        except Exception as e:

                raise Exception("An unexpected error occurred while interacting with the Reset Filter button.") from e


    def Progressbar_Detail_close(self):
        try:
            progress_dtl_close = WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(Projects.Progressbar_Detail_page_Close_button)
            )

        # Wait for the element to be clickable
            WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(Projects.Progressbar_Detail_page_Close_button)
            )

            progress_dtl_close.click()
            return None

        except StaleElementReferenceException:

        # In case the element became stale, try locating it again

            print("Element became stale, re-locating the element.")

            return self.end_date_picker()  # Recursive call to re-locate and click again

        except TimeoutException as e:

            raise Exception("Progressbar detail page not clickable within the timeout") from e

        except Exception as e:

            raise Exception("An unexpected error occurred while interacting with the Reset Filter button.") from e
