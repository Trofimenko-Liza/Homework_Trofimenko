from lesson_25.Homework21_Trofimenko.pages.Home_page import HomePage
from selenium.webdriver import Chrome


class Cookies(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cookies(self, driver):
        self._driver = driver
        return driver.get_cookies()


class LocalStorage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_local_storage(self, driver):
        self._driver = driver
        return driver.execute_script("window.localStorage['test'] = 'Liza_Test_value'")
