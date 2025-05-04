import allure
import pytest

from tests.utils.helpers import safe_click
from tests.pageObjects.pom.dashboard import Dashboard


@allure.epic("Fovero Dashboard Test")
@allure.feature("TC#3 - Validate Dashboard Elements")
@pytest.mark.positive
def test_validate_dashboard_elements(driver):
    dashboard = Dashboard(driver)

    with allure.step("Accessing main Fovero Dashboard"):
        safe_click(dashboard.fovero_dashboardd, "Fovero Dashboard")

    with allure.step("Navigating Punch In/Out Section"):
        safe_click(dashboard.punch_inn_out_back_button, "Punch In/Out Back Button")

    with allure.step("Returning via Sidebar"):
        safe_click(dashboard.sidebar_menu_back_button, "Sidebar Menu Back Button")

    with allure.step("Opening and closing recent timesheet"):
        safe_click(dashboard.recent_timesheet, "Recent Timesheet")
        safe_click(dashboard.close_recent_timesheet, "Close Recent Timesheet")

    with allure.step("Viewing and closing report timesheet"):
        safe_click(dashboard.view_recent_timesheet, "View Report Timesheet")
        safe_click(dashboard.close_report_timesheet, "Close Report Timesheet")

    with allure.step("Applying and exiting leave application"):
        safe_click(dashboard.apply_leave_button, "Apply Leave Button")
        safe_click(dashboard.apply_leave_back_button, "Back Button from Apply Leave")

    with allure.step("Using Sidebar and returning to dashboard"):
        safe_click(dashboard.sidebarr_menu_back_button, "Sidebar Back Button (Alternate)")
        safe_click(dashboard.go_to_dashboard, "Return to Dashboard")
