from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_25.Homework21_Trofimenko.core.locator import Locator
from selenium.webdriver import Chrome

class HomePage:
    def __init__(self, driver):
        self._driver = driver
        self._web_driver_wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_appears(self, locator:Locator):
        return self._web_driver_wait.until(
            EC.presence_of_element_located(locator.to_tuple())
        )

    def _click(self, locator: Locator):
        self._wait_until_element_appears(locator).click()

class CookiesLocalStorage():
    def __init__(self):
        self._driver = None

    def get_cookies(self, driver):
        self._driver = driver
        return driver.get_cookies()

    def set_local_storage(self, driver):
        self._driver = driver
        return driver.execute_script("window.localStorage['test'] = 'Liza_Test_value'")