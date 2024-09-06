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

    # STEP 1: Entering the BUY NOW tab
    buynow_button_xpath = '//*[@id="tyche_products-1"]/div/div[3]/div/div/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, buynow_button_xpath)))
    base_page.click_element(By.XPATH, buynow_button_xpath)

    # STEP 2: Selecting a topic of discussion
    topic_xpath = '//*[@id="main"]/section/div/div/div[1]/div[2]/div/p/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, topic_xpath)))
    base_page.click_element(By.XPATH, topic_xpath)

    # STEP 3: Click the REPLY button
    reply_button_xpath = '//*[@id="div-comment-7073"]/div[2]/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, reply_button_xpath)))
    base_page.click_element(By.XPATH, reply_button_xpath)

    # STEP 4: Enter a comment and complete the remaining required fields
    comment_xpath = '//*[@id="comment"]'
    author_xpath = '//*[@id="author"]'
    email_xpath = '//*[@id="email"]'

    wait.until(EC.visibility_of_element_located((By.XPATH, comment_xpath)))
    base_page.fill_text_field(By.XPATH, comment_xpath, "Losowy text - test forum2")

    wait.until(EC.visibility_of_element_located((By.XPATH, author_xpath)))
    base_page.fill_text_field(By.XPATH, author_xpath, "user_test07")

    wait.until(EC.visibility_of_element_located((By.XPATH, email_xpath)))
    base_page.fill_text_field(By.XPATH, email_xpath, "user_test07@gmail.com")

    # STEP 5: Press the POST COMMENT button.
    submit_button_xpath = '//*[@id="submit"]'
    wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
    base_page.click_element(By.XPATH, submit_button_xpath)

    # STEP 6: Return to main pageę
    home_button_xpath = '//*[@id="masthead"]/div/div/div/div/a'
    wait.until(EC.element_to_be_clickable((By.XPATH, home_button_xpath)))
    base_page.click_element(By.XPATH, home_button_xpath)

    print("SUCCESSFUL CASE")

    time.sleep(5)
    # input("Naciśnij ENTER, aby zamknąć przeglądarkę...")
    # driver.quit()
