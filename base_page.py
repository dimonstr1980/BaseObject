from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://ya.ru"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Not found {locator}!")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Not found {locator}!")
