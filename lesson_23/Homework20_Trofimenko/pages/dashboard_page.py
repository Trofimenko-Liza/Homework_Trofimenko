
from lesson_23.Homework20_Trofimenko.pages.Home_page import HomePage
from selenium.webdriver.chrome.webdriver import WebDriver
from lesson_23.Homework20_Trofimenko.pages.category_sale import CategoryPickPage
from lesson_23.Homework20_Trofimenko.core.locator import Locator
from lesson_23.Homework20_Trofimenko.locators.dashboard_locator import DashboardLocatorsCollection


class Dashboard(HomePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__sale_locator = DashboardLocatorsCollection().sale_locator

    def click_on_sale(self):
        self._click(Locator(*self.__sale_locator))

    def choose_subcategory(self, name):
        self._click(Locator('xpath', f"/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]/a"))
        return CategoryPickPage(self._driver)






