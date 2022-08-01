from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def element_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def element_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

