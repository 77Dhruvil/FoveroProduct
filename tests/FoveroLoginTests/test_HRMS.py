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

