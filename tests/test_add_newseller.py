import sys
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from pages.base_page import BasePage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


@pytest.fixture(scope="module")
def setup_driver():
    driver_path = "add path to msedgedriver.exe"
    service = EdgeService(driver_path)
    options = EdgeOptions()
    options.add_argument("--inprivate")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Edge(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_user_subscription(setup_driver):
    driver = setup_driver
    driver.get("https://skleptest.pl/")
    wait = WebDriverWait(driver, 10)
    base_page = BasePage(driver)

    # STEP 1: Switch to user account
    account_button_xpath = '//*[@id="page"]/header[1]/div/div/div/ul/li[3]/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, account_button_xpath)))
    base_page.click_element(By.XPATH, account_button_xpath)

    # STEP 2: Complete the Name field
    name_field_class = 'ig_es_form_field_name'
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, name_field_class)))
    base_page.fill_text_field(By.CLASS_NAME, name_field_class, "USERT06")

    # STEP 3: Complete the E-Mail field
    email_field_xpath = '/html/body/div/footer[1]/div/div/div/div[4]/div/div/form/div[2]/label/input'
    wait.until(EC.presence_of_element_located((By.XPATH, email_field_xpath)))
    base_page.fill_text_field(By.XPATH, email_field_xpath, "userT06@gmail.com")

    # STEP 4: Press the “Subscribe” button.
    subscribe_button_xpath = '/html/body/div/footer[1]/div/div/div/div[4]/div/div/form/input[9]'
    wait.until(EC.element_to_be_clickable((By.XPATH, subscribe_button_xpath)))
    base_page.click_element(By.XPATH, subscribe_button_xpath)

    # Wait a while for the effects of the action
    wait.until(EC.invisibility_of_element_located((By.ID, 'spinner-image')))  # Assume spinner indicates completion

    # STEP 5: Return to home page
    home_button_xpath = '//*[@id="masthead"]/div/div/div/div/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath)))
    base_page.click_element(By.XPATH, home_button_xpath)

    print("SUCCESSFUL CASE")
