
from lesson_25.Homework21_Trofimenko.pages.Home_page import HomePage
from selenium.webdriver.chrome.webdriver import WebDriver
from lesson_25.Homework21_Trofimenko.pages.category_sale import CategoryPickPage
from lesson_25.Homework21_Trofimenko.core.locator import Locator
from lesson_25.Homework21_Trofimenko.locators.dashboard_locator import DashboardLocatorsCollection
from lesson_25.Homework21_Trofimenko.pages.login_form import LoginForm


class Dashboard(HomePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__sale_locator = DashboardLocatorsCollection().sale_locator

    def click_on_sale(self):
        self._click(Locator(*self.__sale_locator))

    def choose_subcategory(self, name):
        self._click(Locator('xpath', f"/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]/a"))
        return CategoryPickPage(self._driver)

    def login_form(self):
        self._click(Locator('xpath', "//div [ @ data-popup-handler='auth']"))
        return LoginForm(self._driver)








