import sys
import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from pages.home_page import HomePage
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


def test_shirts_page_titles(setup_driver):
    driver = setup_driver
    driver.get("https://skleptest.pl/")
    wait = WebDriverWait(driver, 10)
    base_page = BasePage(driver)
    home_page = HomePage(driver)

    # STEP 1: Entering the SHOES tab
    home_page.go_to_shoes()
    time.sleep(5)

    # STEP 2: Adding items to the cart
    add_to_cart_xpath_1 = '//*[@id="page"]/div/div/div[2]/div/ul/li[2]/a[2]'
    add_to_cart_element_1 = wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath_1)))
    add_to_cart_element_1.click()
    time.sleep(5)
    add_to_cart_xpath_2 = '//*[@id="page"]/div/div/div[2]/div/ul/li[3]/a[2]'
    add_to_cart_element_2 = wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath_2)))
    add_to_cart_element_2.click()
    time.sleep(5)

    # STEP 3: Move to the shopping cart
    go_to_cart_xpath = '//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a'
    go_to_cart_element = wait.until(EC.element_to_be_clickable((By.XPATH, go_to_cart_xpath)))
    go_to_cart_element.click()

    # STEP 4: Go to order details
    go_to_checkout_xpath = '// *[ @ id = "post-6"] / div[2] / div / div / div / a'
    go_to_checkout_element = wait.until(EC.element_to_be_clickable((By.XPATH, go_to_checkout_xpath)))
    go_to_checkout_element.click()

    # STEP 5: Complete all necessary fields
    fill_field_details = [
        ('// *[ @ id = "billing_first_name"]', "Test01_first_name"),
        ('// *[ @ id = "billing_last_name"]', "Test01_last_name"),
        ('// *[ @ id = "billing_address_1"]', "Ul. Testerska 51/4"),
        ('// *[ @ id = "billing_postcode"]', "50-111"),
        ('// *[ @ id = "billing_city"]', "Poznan"),
    ]

    for xpath, value in fill_field_details:
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        base_page.fill_text_field(By.XPATH, xpath, value)

    # STEP 6: Complete the remaining fields:
    email_id='billing_email'
    base_page.fill_text_field(By.ID,email_id,"bartosz_test@gmail.com")


    # Selecting a country from the SELECT list
    select_country_xpath = '//*[@id="billing_country"]/option[71]'
    select_country_element = wait.until(EC.element_to_be_clickable((By.XPATH, select_country_xpath)))
    select_country_element.click()
    time.sleep(5)

    # Selecting a radio-button
    base_page.select_radio_button(By.XPATH, '// *[ @ id = "payment_method_cheque"]')
    time.sleep(5)

    # STEP 6: Pressing the order button
    place_order_xpath = '// *[ @ id = "place_order"]'
    place_order_element = wait.until(EC.element_to_be_clickable((By.XPATH, place_order_xpath)))
    place_order_element.click()


    print("SUCCESSFUL CASE")
