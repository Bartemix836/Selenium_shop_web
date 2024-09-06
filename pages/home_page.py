from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def go_to_shirts(self):
        self.hover_over_element(By.XPATH, "/html/body/div/header[2]/nav/div/div/div/ul/li[3]")
        self.click_element(By.XPATH, "//a[@title='Shirts']")

    def go_to_shoes(self):
        self.hover_over_element(By.XPATH, "/html/body/div/header[2]/nav/div/div/div/ul/li[3]")
        self.click_element(By.XPATH, "//a[@title='Shoes']")
