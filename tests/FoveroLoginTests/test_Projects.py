import allure
import pytest
#from tests.FoveroLoginTests.test_FoveroLogin import test_FoveroLogin_Positive
from tests.pageObjects.pom.HRMS import HRMS
from tests.pageObjects.pom.Projects import Projects
from tests.pageObjects.pom.dashboard import Dashboard


@allure.epic("Fovero Projects Test")
@allure.feature("TC#4 - Validate Projects Elements")
def test_Projects(driver):
    projects = Projects(driver)
    projects.get_Projects()
