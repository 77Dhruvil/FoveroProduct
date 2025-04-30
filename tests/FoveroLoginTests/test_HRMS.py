import time

import allure
import pytest
#from tests.FoveroLoginTests.test_FoveroLogin import test_FoveroLogin_Positive
from tests.pageObjects.pom.HRMS import HRMS
from tests.pageObjects.pom.dashboard import Dashboard


@allure.epic("Fovero HRMS Test")
@allure.feature("TC#4 - Validate HRMS Elements")
def test_HRMS(driver):
    hrms = HRMS(driver)

    try:
        hrms.hrms_click_sidebarmenu().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        hrms.leaves_page().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        hrms.upcoming_leave_tab()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)
    try:
        hrms.upcoming_leave_detail_click().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)
    try:
        hrms.upcoming_leave_detail_page_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        hrms.history_leave_tab().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        hrms.history_detail_page().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        hrms.history_detail_page_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)
    try:
        hrms.verify_casual_leave().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)
    try:
        hrms.verify_total_leave().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)
    try:
        hrms.apply_leave_button().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.leave_type_dropdown_value_select()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.leave_to_field_value_select()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.from_date_field().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)
    try:
        hrms.from_date_select()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.to_date_field().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.to_date_select()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.duration_select()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.cancel_button().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.leave_list_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.leave_logs().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.leave_logs_back_button().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.attendance_productivity_report().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.productivity_report_status_dropdown().click()
    except Exception as e:
        pytest.fail(str(e))

    time.sleep(5)

    try:
        hrms.productivity_report_status_dropdown_value().click()
    except Exception as e:
        pytest.fail(str(e))