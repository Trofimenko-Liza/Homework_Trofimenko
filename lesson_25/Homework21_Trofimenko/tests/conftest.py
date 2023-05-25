from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from lesson_25.Homework21_Trofimenko.pages.dashboard_page import Dashboard
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('lesson_25/driver/chromedriver.exe')
    driver.get("https://makeup.com.ua/")
    driver.maximize_window()
    driver.set_window_size(2000,1600)
    print(driver.get_cookies())

    yield driver

    driver.quit()

@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
