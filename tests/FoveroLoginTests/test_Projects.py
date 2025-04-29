import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    time.sleep(5)
    try:
        projects.filter_button_click()
    except Exception as e:
        pytest.fail(str(e))
    print("1")

    try:
        projects.filterr_search_button().click()
    except Exception as e:
        pytest.fail(str(e))

    try:
        projects.filter_button().click()
    except Exception as e:
        pytest.fail(str(e))
    time.sleep(5)
    print("222")

    try:
        projects.Reset_button().click()
    except Exception as e:
        pytest.fail(str(e))


    time.sleep(5)
    try:

        projects.progress_button_click().click()
    except Exception as e:
        pytest.fail(str(e))


    print("dsad sadsa")
    time.sleep(5)
    try:
        projects.Date_picker().click()
    except Exception as e:
        pytest.fail(str(e))
    print("vvvvvvvvv")
    time.sleep(5)
    try:
        projects.start_date_picker().click()
    except Exception as e:
        pytest.fail(str(e))
    time.sleep(5)

    try:
        projects.end_date_picker().click()
    except Exception as e:
        pytest.fail(str(e))
    time.sleep(5)
    try:
        projects.Progressbar_Detail_close().click()
    except Exception as e:
        pytest.fail(str(e))


# def safe_click(element_func, description="element"):
#     try:
#         element = element_func()
#         if element is not None:
#             element.click()
#     except Exception as e:
#         pytest.fail(f"Failed to interact with {description}: {str(e)}")
#
#
# def test_Projects(driver):
#     projects = Projects(driver)
#
#     safe_click(projects.get_sidebar_menu_projects, "Sidebar menu Projects")
#     safe_click(projects.get_project_name_click, "Project Name")
#     safe_click(projects.get_project_Estimation_tab, "Estimation Tab")
#     safe_click(projects.get_Estimation_Department_click, "Estimation Department")
#     safe_click(projects.Estimation_view_popup_close, "Estimation View Close Button")
#     safe_click(projects.Document_tabb_click, "Document Tab")
#     safe_click(projects.Edit_project_back_button, "Back Button")
#     safe_click(projects.search_bar, "Search Bar")
#     safe_click(projects.filter_button, "Filter Button")
#     time.sleep(5)
#     safe_click(projects.filter_button_click, "Filter Apply")
#     time.sleep(5)
#     safe_click(projects.filterr_search_button, "Filter Search Button")
#     safe_click(projects.Reset_button, "Reset Button")
#     safe_click(projects.progress_button_click, "Progress Button")
#     safe_click(projects.Date_picker, "Date Picker")
#     safe_click(projects.start_date_picker, "Start Date")
#     safe_click(projects.end_date_picker, "End Date")
#     safe_click(projects.Progressbar_Detail_close, "Progress Bar Detail Close")
#     print("Totally completed")


