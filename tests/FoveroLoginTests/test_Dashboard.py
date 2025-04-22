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
        dashboard.get_Fovero_Dashboardd()

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



    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Dashboard_Failure",
                      attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed due to exception: {e}")
