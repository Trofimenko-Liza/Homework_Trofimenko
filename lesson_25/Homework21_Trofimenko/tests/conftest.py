from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from lesson_25.Homework21_Trofimenko.pages.dashboard_page import Dashboard
from lesson_25.Homework21_Trofimenko.pages.Cookies import Cookies
from lesson_25.Homework21_Trofimenko.pages.Cookies import LocalStorage
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('lesson_25/driver/chromedriver.exe')
    driver.get("https://makeup.com.ua/")
    driver.maximize_window()
    driver.set_window_size(2000,1600)

    yield driver

    driver.quit()

@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)

@pytest.fixture
def cookies(driver):
    yield Cookies(driver)

@pytest.fixture
def local_storage(driver):
    yield LocalStorage(driver)
