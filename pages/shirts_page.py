from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShirtsPage(BasePage):
    def get_product_titles(self):
        clots = self.driver.find_elements(By.XPATH, "//h2[contains(@class,'woocommerce-loop-product__title')]")
        return [clot.text for clot in clots]
