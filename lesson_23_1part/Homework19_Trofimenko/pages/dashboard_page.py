from lesson_23_1part.Homework19_Trofimenko.pages.Home_page import HomePage
from selenium.webdriver.chrome.webdriver import WebDriver

class Dashboard(HomePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__nav_bar_locator = ('xpath', "/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[1]/a")

    def click_on_sale(self):
        element = self._wait_until_element_appears(self.__nav_bar_locator)
        element.click()

    def choose_sale_parfums(self, name):
        locator = ('xpath', f"/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]/a")
        element = self._wait_until_element_appears(locator)
        element.click()