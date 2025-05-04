import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def safe_click(element_func, description="", timeout=10):
#     with allure.step(f"Click: {description}"):
#         try:
#             element = element_func()
#             if element:
#                 # Wait until element is clickable
#                 WebDriverWait(element._parent, timeout).until(EC.element_to_be_clickable(element))
#                 element.click()
#                 allure.attach(body=f"Clicked: {description}", name=description, attachment_type=allure.attachment_type.TEXT)
#             else:
#                 msg = f"[WARN] Element not found: {description}"
#                 allure.attach(body=msg, name=f"Not Found: {description}", attachment_type=allure.attachment_type.TEXT)
#                 pytest.fail(msg)
#         except Exception as e:
#             allure.attach(body=str(e), name=f"Failed: {description}", attachment_type=allure.attachment_type.TEXT)
#             pytest.fail(f"[ERROR] Failed to click {description}: {str(e)}")

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
