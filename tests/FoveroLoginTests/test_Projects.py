import allure
import pytest

from tests.utils.helpers import safe_click, safe_action
from tests.pageObjects.pom.Projects import Projects


@allure.epic("Fovero Projects Test")
@allure.feature("TC#4 - Validate Projects Elements")
@pytest.mark.positive
def test_Projects(driver):
    projects = Projects(driver)

    with allure.step("Accessing Project from Sidebar"):
        safe_click(projects.Sidebar_menu_project, "Sidebar Project Menu")
        safe_click(projects.project_name_click, "Project Name")

    with allure.step("Checking Estimation Tab and Department View"):
        safe_click(projects.Project_Esitmation_tab, "Estimation Tab")
        safe_click(projects.Estimation_department_click, "Estimation Department View")
        safe_click(projects.Estimation_view_popup_close, "Close Estimation View Popup")

    with allure.step("Switching to Document Tab"):
        safe_click(projects.Document_tabb_click, "Document Tab")

    with allure.step("Returning from Edit Project Page"):
        safe_click(projects.Edit_project_back_button, "Back from Edit Project")

    with allure.step("Performing Search and Filter Operation"):
        safe_click(projects.search_bar, "Search Bar")
        safe_click(projects.filter_button, "Filter Button")
        safe_action(projects.filter_button_click, "Click Inside Filter Dropdown")
        safe_click(projects.filterr_search_button, "Filter Search Button")

        # Reopen filter and reset
        safe_click(projects.filter_button, "Filter Button (Reopen)")
        safe_click(projects.Reset_button, "Reset Filter")

    with allure.step("Validating Progress Details with Date Selection"):
        safe_click(projects.progress_button_click, "Progress Button")
        safe_click(projects.Date_picker, "Date Picker")
        safe_click(projects.start_date_picker, "Start Date")
        safe_click(projects.end_date_picker, "End Date")
        safe_click(projects.Progressbar_Detail_close, "Close Progressbar Detail")
