import sys
import os
import pytest
import time
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
    driver_path = "C:/Users/barte/PycharmProjects/selenium_kurs/drivers/msedgedriver.exe"
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

    # Open page
    driver.get("https://skleptest.pl/")
    driver.maximize_window()

    #Initializing the page
    base_page = BasePage(driver)
    wait = WebDriverWait(driver, 10)

    #STEP 1: Enter the password in the text field.
    search_field_xpath = '//*[@id="search-field-top-bar"]'
    wait.until(EC.visibility_of_element_located((By.XPATH, search_field_xpath)))
    base_page.fill_text_field(By.XPATH, search_field_xpath, "Amari Shirt")

    #STEP 2: Pressing the Search button
    search_button_xpath = '//*[@id="search-top-bar-submit"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, search_button_xpath)))
    base_page.click_element(By.XPATH, search_button_xpath)

    #STEP 3: Going into the details of the item
    product_details_xpath = '//*[@id="post-62"]/header/div/div[2]/h2/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, product_details_xpath)))
    base_page.click_element(By.XPATH, product_details_xpath)

    print("SUCCESSFUL CASE")

    time.sleep(5)

