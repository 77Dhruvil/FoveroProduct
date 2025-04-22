import allure
import pytest
from tests.FoveroLoginTests.test_FoveroLogin import test_FoveroLogin_Positive
from tests.pageObjects.pom.HRMS import HRMS
from tests.pageObjects.pom.dashboard import Dashboard


@allure.epic("Fovero HRMS Test")
@allure.feature("TC#4 - Validate HRMS Elements")
def test_HRMS(driver):
    test_FoveroLogin_Positive(driver)
    hrms = HRMS(driver)
    hrms.get_HRMS()
    print("Completed")
    if hrms.is_upcoming_leaves_present():
        print("Test Passed ✅ - Upcoming leaves are present.")
    else:
        print("Test Failed ❌ - No upcoming leaves found.")
        driver.save_screenshot("no_upcoming_leaves.png")

    if hrms.is_history_leaves_present():
        print("Test Passed ✅ - History leaves are present.")
    else:
        print("Test Failed ❌ - No History leaves found.")
        driver.save_screenshot("no_history_leaves.png")
