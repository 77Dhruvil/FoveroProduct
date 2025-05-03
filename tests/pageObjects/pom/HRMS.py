import time
import keyboard
import pyautogui

import pytest
import allure
from selenium.common import StaleElementReferenceException, TimeoutException, NoSuchElementException

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
    Upcomming_leave_data_click = (By.XPATH,'//*[@id="cell-1-21991"]/div/a')
    Upcomming_leave_detail_page_backbutton = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[1]/div[1]/div/a')
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
    End_To_date_field = (By.NAME,"end_date")
    Duration_selection = (By.XPATH,'//*[@id="leaveDays.[0].selectedDuration"]/div')
    Leave_Reason = (By.ID,"leave_reason")
    Cancel_button = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[2]/div[1]/div/div/form/div[6]/div/button[2]')
    Back_button_Leave_List = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[1]/div[1]/a')
    Leave_logs = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div/div[1]/div/div[2]/div[2]/a')
    Back_button_Leave_Logs = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div[1]/div/div[1]/div/a')
    Attendance_Productivity_Report_click = (By.XPATH,'//*[@id="root"]/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div[1]/a/button')
    Productivity_report_Status_dropdown_click = (By.XPATH,'//*[@id="filter"]/div')
    Productivity_report_Status_dropdown_value = (By.XPATH,'//*[@id="filter"]/div/div[1]/div[2]')


    def get_sidebar_menu_HRMS(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Sidebar_menu_HRMS))

    def get_Leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Leaves))

    def get_upcomming_leaves(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(HRMS.Upcomming_Leaves))

    def get_upcoming_leave_data_click(self):
        return WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(HRMS.Upcomming_leave_data_click))

    def get_upcoming_leave_detail_page_back_button_click(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.Upcomming_leave_detail_page_backbutton))
    def is_no_records_message_displayed(self):

        try:
            element = self.driver.find_element(self.No_upcoming_leaves)
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

        # 4. Select the day
        day_cell = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div[2]/div/div/div/form/div[4]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]')))
        day_cell.click()
        time.sleep(10)

    def get_end_to_date_field(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.End_To_date_field))

    def get_end_to_date_picker(self,year,month,day):

        wait = WebDriverWait(self.driver, 10)

        # 1. Click on the "From" date field to open the date picker
        date_field = wait.until(EC.element_to_be_clickable((By.NAME, "end_date")))
        date_field.click()

        # 2. Select the year
        year_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="root"]/div[2]/div[3]/div[2]/div[1]/div/div/form/div[4]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select')))
        year_dropdown.click()

        year_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="root"]/div[2]/div[3]/div[2]/div[1]/div/div/form/div[4]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[1]')))
        year_option.click()

        # 3. Select the month
        month_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="root"]/div[2]/div[3]/div[2]/div[1]/div/div/form/div[4]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select')))
        month_dropdown.click()
        month_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="root"]/div[2]/div[3]/div[2]/div[1]/div/div/form/div[4]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[4]')))
        month_option.click()
        time.sleep(5)

        # 4. Select the day
        day_cell = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="root"]/div[2]/div[3]/div[2]/div[1]/div/div/form/div[4]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[6]')))
        day_cell.click()


    def get_duration_selection(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.Duration_selection))

    def get_leave_reason(self):
        return (WebDriverWait(self.driver,timeout=10).until
                (EC.presence_of_element_located(HRMS.Leave_Reason))
            )


    def get_cancel_button(self):
        return (WebDriverWait(self.driver, timeout=10).until
                (EC.presence_of_element_located(HRMS.Cancel_button))
                )

    def get_Back_button_leave_list(self):
        return (WebDriverWait(self.driver, timeout=10).until
                (EC.presence_of_element_located(HRMS.Back_button_Leave_List))
                )

    def get_Leave_logs(self):
        return (WebDriverWait(self.driver, timeout=10).until
                (EC.presence_of_element_located(HRMS.Leave_logs))
                )

    def get_Back_button_leave_logs(self):
        return (WebDriverWait(self.driver, timeout=10).until
                (EC.presence_of_element_located(HRMS.Back_button_Leave_Logs))
                )

    def get_attendance_productivity_report(self):
        return WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located(HRMS.Attendance_Productivity_Report_click)
        )

    def get_productivity_report_statu_dropdown_click(self):
        return WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located(HRMS.Productivity_report_Status_dropdown_click))

    def get_productivity_report_status_dropdown_value(self):
        return WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(HRMS.Productivity_report_Status_dropdown_value))


    def hrms_click_sidebarmenu(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Sidebar_menu_HRMS))
        except TimeoutException as e:
            raise Exception("Sidebar menu is not clickable") from e


    def leaves_page(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Leaves))
        except TimeoutException as e:
            raise Exception("Leaves menu is not clickable") from e


    def upcoming_leave_tab(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Upcomming_Leaves))
        except TimeoutException as e:
            raise Exception("Upcoming leave menu is not clickable") from e

    def upcoming_leave_detail_click(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(
                EC.element_to_be_clickable(HRMS.Upcomming_leave_data_click)
            )
        except TimeoutException:
            print("No upcoming leave data found.")
            return None

    def upcoming_leave_detail_page_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(HRMS.Upcomming_leave_detail_page_backbutton)
            )
        except TimeoutException:
            print("No Upcoming Detail page found --- Skip")
            return None

    def history_leave_tab(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.History_Leaves))
        except TimeoutException as e:
            raise Exception("History leave tab is not clickable or visible") from e



    time.sleep(5)

    def history_detail_page(self):
        try:
            return WebDriverWait(self.driver, timeout=5).until(
                EC.element_to_be_clickable(HRMS.Detail_History_Leaves)
            )
        except TimeoutException:
            print("No history leave data found.")
            return None

    time.sleep(5)

    def history_detail_page_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.element_to_be_clickable(HRMS.Back_Button_Detail_History_leaves)
            )
        except TimeoutException:
            print("No History Detail page found --- Skip")
            return None

    time.sleep(5)

    def verify_casual_leave(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Verify_casual_leaves))
        except TimeoutException as e:
            raise Exception("Casual leave is not as per expected") from e

    def verify_total_leave(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Verify_Total_leaves))
        except TimeoutException as e:
                raise Exception("Total leave is not as per expected") from e

    def apply_leave_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Apply_leave_button))
        except TimeoutException as e:
                raise Exception("Apply leave button is not clickable") from e

    def leave_type_dropdown_value_select(self):

         try:
            self.get_Leave_type_Dropdown()
         except (TimeoutException, NoSuchElementException) as e:
            pytest.fail("Leave type dropdown is not opened")


    def leave_to_field_value_select(self):

         try:
            self.get_To_Dropdown(driver=self.driver, user_list=['Manish Patel', 'Tejas Patel'])
         except (TimeoutException, NoSuchElementException) as e:
            pytest.fail("Value is not selected from the dropdown")


    def from_date_field(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Start_From_date_field))
        except TimeoutException as e:
                raise Exception("Start date field click is not working") from e

    def from_date_select(self):

        try:
            self.get_select_date_picker('2025', '4','10')
        except (TimeoutException, NoSuchElementException) as e:
            pytest.fail("Sart date value is not selectable")

    def to_date_field(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.End_To_date_field))
        except TimeoutException as e:
                raise Exception("End date field click is not working") from e


    def to_date_select(self):

        try:
            self.get_end_to_date_picker('2025','4','11')
        except (TimeoutException, NoSuchElementException) as e:
            pytest.fail("End date Value   is not Selectable")


    def duration_select(self):

        try:
            self.get_duration_selection().click()
        except (TimeoutException, NoSuchElementException) as e:
            pytest.fail("Duration selection is not working")

        keyboard.write("First Half")
        keyboard.press("enter")

    def leave_reason(self):


        try:
            self.get_leave_reason().send_keys("Need to attend Function")
        except (TimeoutException, NoSuchElementException) as e:
            pytest.fail("Is not clickable and written in the field")

    def cancel_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Cancel_button))
        except TimeoutException as e:
            raise Exception("cancel button Is not clickable") from e

    def leave_list_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Back_button_Leave_List))
        except TimeoutException as e:
            raise Exception("Back button from the list page is not working") from e

    def leave_logs(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Leave_logs))
        except TimeoutException as e:
            raise Exception("User is not able to click on the leave logs") from e


    pyautogui.scroll(-500)  # Scrolls down

    def leave_logs_back_button(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Back_button_Leave_Logs))
        except TimeoutException as e:
            raise Exception("User is not able to click the leave logs back button") from e

    def attendance_productivity_report(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Attendance_Productivity_Report_click))
        except TimeoutException as e:
            raise Exception("User is not able to click on the productivity report") from e




    def productivity_report_status_dropdown(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Productivity_report_Status_dropdown_click))
        except TimeoutException as e:
            raise Exception("User is not able to click on the dropdown") from e



    def productivity_report_status_dropdown_value(self):

        try:
            return WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(HRMS.Productivity_report_Status_dropdown_value))
        except TimeoutException as e:
            raise Exception("User is not able to click on the dropdown") from e

    print("completed")

