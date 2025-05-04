import allure
import pytest
from tests.utils.helpers import safe_click, safe_action
from tests.pageObjects.pom.HRMS import HRMS


@allure.epic("Fovero HRMS Test")
@allure.feature("TC#4 - Validate HRMS Elements")
@pytest.mark.positive
def test_HRMS(driver):
    hrms = HRMS(driver)

    with allure.step("Navigating to Leaves section via Sidebar"):
        safe_click(hrms.hrms_click_sidebarmenu, "HRMS Sidebar Menu")
        safe_click(hrms.leaves_page, "Leaves Page")

    with allure.step("Checking Upcoming Leave Details"):
        safe_action(hrms.upcoming_leave_tab, "Select Upcoming Leave Tab")
        safe_click(hrms.upcoming_leave_detail_click, "Upcoming Leave Detail")
        safe_click(hrms.upcoming_leave_detail_page_back_button, "Back from Upcoming Leave Detail")

    with allure.step("Checking Leave History Details"):
        safe_click(hrms.history_leave_tab, "Leave History Tab")
        safe_click(hrms.history_detail_page, "History Leave Detail")
        safe_click(hrms.history_detail_page_back_button, "Back from History Detail")

    with allure.step("Verifying Leave Info"):
        safe_click(hrms.verify_casual_leave, "Verify Casual Leave")
        safe_click(hrms.verify_total_leave, "Verify Total Leave")

    with allure.step("Starting Leave Application and Cancelling"):
        safe_click(hrms.apply_leave_button, "Apply Leave Button")
        safe_action(hrms.leave_type_dropdown_value_select, "Select Leave Type from Dropdown")
        safe_action(hrms.leave_to_field_value_select, "Select Leave To Value")

        # From Date
        safe_click(hrms.from_date_field, "From Date Field")
        safe_action(hrms.from_date_select, "Select From Date")

        # To Date
        safe_click(hrms.to_date_field, "To Date Field")
        safe_action(hrms.to_date_select, "Select To Date")

        # Duration and Cancel
        safe_action(hrms.duration_select, "Select Duration")
        safe_click(hrms.cancel_button, "Cancel Leave Application")

    with allure.step("Navigating Back to Leave List"):
        safe_click(hrms.leave_list_back_button, "Back to Leave List")

    with allure.step("Checking Leave Logs"):
        safe_click(hrms.leave_logs, "Leave Logs")
        safe_click(hrms.leave_logs_back_button, "Back from Leave Logs")

    with allure.step("Verifying Attendance Productivity Report"):
        safe_click(hrms.attendance_productivity_report, "Attendance Productivity Report")
        safe_click(hrms.productivity_report_status_dropdown, "Status Dropdown")
        safe_click(hrms.productivity_report_status_dropdown_value, "Select Status Value")
