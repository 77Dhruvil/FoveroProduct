import time

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
    try:
        projects.get_sidebar_menu_projects().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.get_project_name_click().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.get_project_Estimation_tab().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.get_Estimation_Department_click().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.Estimation_view_popup_close().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.Document_tabb_click().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.Edit_project_back_button().click()
    except Exception as e:
        pytest.fail(str(e))


    try:
        projects.search_bar().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.filter_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.filter_button_click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.filterr_search_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.Reset_button()
    except Exception as e:
        pytest.fail(str(e))


    try:
        projects.progress_button_click().click()
    except Exception as e:
        pytest.fail(str(e))
    time.sleep(5)

    try:
        projects.Date_picker().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.start_date_picker().click()
    except Exception as e:
        pytest.fail(str(e))


    try:
        projects.end_date_picker().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.Progressbar_Detail_close().click()
    except Exception as e:
        pytest.fail(str(e))