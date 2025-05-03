import pytest
import allure

def safe_click(element_func, description=""):
    with allure.step(f"Click: {description}"):
        try:
            element = element_func()
            if element:
                element.click()
            else:
                print(f"[WARN] Element not found: {description}")
        except Exception as e:
            pytest.fail(f"[ERROR] Failed to click {description}: {str(e)}")

def safe_action(action_func, description=""):
    with allure.step(description):
        try:
            action_func()
        except Exception as e:
            pytest.fail(f"[ERROR] Failed: {description}: {str(e)}")
