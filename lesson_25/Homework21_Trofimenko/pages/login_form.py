from lesson_25.Homework21_Trofimenko.pages.Home_page import HomePage
from lesson_25.Homework21_Trofimenko.core.locator import Locator


class LoginForm(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_row(self, login_fill:str, password_fill:str):
        login = self._wait_until_element_appears(Locator('xpath', "// input[ @ id = 'login']"))
        login.send_keys(login_fill)
        password = self._wait_until_element_appears(Locator('xpath', "//input [ @id='pw']"))
        password.send_keys(password_fill)
        self._click(Locator('xpath', "//*[@id='form-auth']/div/div/div[4]/button"))
