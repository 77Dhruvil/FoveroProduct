# import  allure
# import pytest
# from tests.FoveroLoginTests.test_FoveroLogin import test_FoveroLogin_Positive, driver
# from tests.pageObjects.pom.dashboard import Dashboard
#
# @allure.epic("Fovero Dashboard Test")
# @allure.feature("TC#3 - Fovero Dashboard  Test")
# @pytest.mark.positive
#
# def test_Fovero_Dashboard(driver):
#
#     test_FoveroLogin_Positive(driver)
#     dashboard = Dashboard(driver)
#     dashboard.get_Fovero_Dashboard()
import time

import allure
import pytest
from tests.FoveroLoginTests.test_FoveroLogin import test_FoveroLogin_Positive
from tests.pageObjects.pom.dashboard import Dashboard


@allure.epic("Fovero Dashboard Test")
@allure.feature("TC#3 - Validate Dashboard Elements")
@pytest.mark.positive
def test_Fovero_Dashboard(driver):
    try:
        # Step 1: Login
        test_FoveroLogin_Positive(driver)

        # Step 2: Navigate to Dashboard
        dashboard = Dashboard(driver)
        dashboard.get_Fovero_Dashboard()


        # Step 3: Validate Productive Hours
        productive_hours = dashboard.get_user_weekly_recorded_hrs_viewall()
        assert productive_hours is not None, "Productive hours not displayed"
        print(f"✅ Productive hours: {productive_hours}")


        todays_birthdays = dashboard.check_birthday_section("Today's")

        if any("No Data Found" in text for text in todays_birthdays):
            print("✅ No one has a birthday today.")
        else:
            print("🎉 Today's Birthdays Found:")
            for bday in todays_birthdays:
                print(f"  - {bday}")

        print("\n✅ Verifying Upcoming Birthdays:")
        upcoming_birthdays = dashboard.check_birthday_section("Upcoming")

        if any("No Data Found" in text for text in upcoming_birthdays):
            print("✅ No upcoming birthdays.")
        else:
            print("🎉 Upcoming Birthdays Found:")
            for bday in upcoming_birthdays:
                print(f"  - {bday}")


    #         # Step 4: Check if Leave/WFH users are listed
#         leave_users = dashboard.get_leave_users()
#         wfh_users = dashboard.get_wfh_users()
#
#         if leave_users or wfh_users:
#             print("✅ Leave/WFH users are listed")
#         else:
#             pytest.fail("❌ No Leave or WFH users found")
#
#         # Step 5: Check Announcements exist
#         announcements = dashboard.get_announcements()
#         assert len(announcements) > 0, "No announcements found"
#         print(f"✅ {len(announcements)} announcement(s) present")
#
#         # Step 6: Validate Timesheet entries
#         timesheets = dashboard.get_recent_timesheets()
#         assert len(timesheets) > 0, "Timesheet entries missing"
#
#         for entry in timesheets:
#             assert 'date' in entry and 'project' in entry and 'hours' in entry, "Timesheet entry is missing details"
#             print(f"✅ Timesheet: {entry['date']} | {entry['project']} | {entry['hours']}h")
#
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Dashboard_Failure",
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed due to exception: {e}")
#
#
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#
# def get_productive_hours(self):
#
#
# # return the text or value from the dashboard element
#
# def get_leave_users(self):
#
#
# # return list of names or elements in Leave section
#
# def get_wfh_users(self):
#
#
# # return list of names or elements in WFH section
#
# def get_announcements(self):
#
#
# # return list of announcement text blocks
#
# def get_recent_timesheets(self):
# # return a list of dicts like [{'date': '2025-04-11', 'project': 'Fovero - Product', 'hours': '8'}]












