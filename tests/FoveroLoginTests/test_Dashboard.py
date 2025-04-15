import  allure
import pytest
from tests.FoveroLoginTests.test_FoveroLogin import test_FoveroLogin_Positive, driver
from tests.pageObjects.pom.dashboard import Dashboard

@allure.epic("Fovero Dashboard Test")
@allure.feature("TC#3 - Fovero Dashboard  Test")
@pytest.mark.positive

def test_Fovero_Dashboard(driver):

    test_FoveroLogin_Positive(driver)
    dashboard = Dashboard(driver)
    dashboard.get_Fovero_Dashboard()








