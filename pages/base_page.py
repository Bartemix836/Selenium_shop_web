from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def hover_over_element(self, by, value):
        try:
            element_to_hover_over = self.driver.find_element(by, value)
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()
            print("Hovered over element")
        except Exception as e:
            print(f"Failed to hover over element: {e}")

    def click_element(self, by, value):
        try:
            element_to_click = self.driver.find_element(by, value)
            element_to_click.click()
            print("Clicked on element")
        except Exception as e:
            print(f"Failed to click on element: {e}")

    def fill_text_field(self, by, value, text):
        try:
            text_field = self.driver.find_element(by, value)
            text_field.send_keys(text)
            print(f"Entered text '{text}' into text field")
        except Exception as e:
            print(f"Failed to enter text into text field: {e}")

    def select_radio_button(self, by, value):
        try:
            radio_button = self.driver.find_element(by, value)
            if not radio_button.is_selected():
                radio_button.click()
                print(f"Selected radio button with XPATH: {value}")
            else:
                print(f"Radio button with XPATH: {value} is already selected")
        except Exception as e:
            print(f"Failed to select radio button: {e}")

    def select_dropdown_option_by_xpath(self, xpath):
        try:
            option = self.driver.find_element(By.XPATH, xpath)
            option.click()
            print(f"Selected dropdown option with XPATH: {xpath}")
        except Exception as e:
            print(f"Failed to select dropdown option: {e}")
