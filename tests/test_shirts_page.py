import sys
import os
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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


def test_shirts_page_titles(setup_driver):
    driver = setup_driver
    driver.get("https://skleptest.pl/")
    wait = WebDriverWait(driver, 10)
    base_page = BasePage(driver)


    # STEP 1: Hover over the CATEGORIES tab.
    categories_xpath = '//*[@id="menu-item-123"]/a'  # XPath do zakładki CATEGORIES
    categories_element = wait.until(EC.visibility_of_element_located((By.XPATH, categories_xpath)))
    time.sleep(5)

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Hovering the cursor over the CATEGORIES element
    actions.move_to_element(categories_element).perform()

    # STEP 2: Click SHIRTS from the drop-down list
    shirts_link_xpath = '//*[@id="menu-item-125"]/a'  # XPath SHIRTS
    shirts_element = wait.until(EC.element_to_be_clickable((By.XPATH, shirts_link_xpath)))
    shirts_element.click()

    # STEP2A:Selecting the item in question
    shirtdetails_xpath='//*[@id="page"]/div/div/div[2]/div/ul/li[5]/a[1]'
    shirtdetails_element=wait.until(EC.element_to_be_clickable((By.XPATH,shirtdetails_xpath)))
    base_page.click_element(By.XPATH,shirtdetails_xpath)

    # STEP 3: Return to the SHIRT section
    shirt_section_xpath='/html/body/div[1]/div/div/div/div/div/div[2]/div[2]/span[1]/a[1]'
    shirt_section=wait.until(EC.element_to_be_clickable((By.XPATH,shirt_section_xpath)))
    base_page.click_element(By.XPATH,shirt_section_xpath)


    print("SUCCESSFUL CASE")

    # Czas na ręczne zakończenie testu
    time.sleep(5)
