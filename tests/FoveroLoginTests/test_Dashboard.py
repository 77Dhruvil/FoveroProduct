import allure
import pytest
#from tests.FoveroLoginTests.test_FoveroLogin import test_FoveroLogin_Positive
from tests.pageObjects.pom.dashboard import Dashboard


@allure.epic("Fovero Dashboard Test")
@allure.feature("TC#3 - Validate Dashboard Elements")
@pytest.mark.positive
def test_Fovero_Dashboard(driver):

    dashboard = Dashboard(driver)

    try:
        dashboard.fovero_dashboardd().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.punch_inn_out_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.sidebar_menu_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.recent_timesheet().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.close_recent_timesheet().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.view_recent_timesheet().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.close_report_timesheet().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.apply_leave_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.apply_leave_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.sidebarr_menu_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        dashboard.go_to_dashboard().click()
    except Exception as e:
        pytest.fail(str(e))
    print("Completed Whole test case")
