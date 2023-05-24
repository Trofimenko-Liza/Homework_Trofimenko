from lesson_23.Homework20_Trofimenko.pages.Home_page import HomePage
from lesson_23.Homework20_Trofimenko.pages.sale_subcategory_parfums import SaleSubcategoryPerfumes
from lesson_23.core.locator import Locator


class CategoryPickPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__perfumes_locator = Locator('xpath', f"/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]/a")

    def choose_perfumes_selection(self):
        self._click(self.__perfumes_locator)
        return SaleSubcategoryPerfumes(self._driver)

