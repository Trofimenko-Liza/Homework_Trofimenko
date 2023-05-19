from selenium.webdriver import Chrome
from lesson_23_1part.Homework19_Trofimenko.pages.dashboard_page import Dashboard

import pytest


@pytest.fixture(scope="session")
def driver():
    driver = Chrome('lesson_23_1part/Homework19_Trofimenko/drivers/chromedriver.exe')
    driver.get("https://makeup.com.ua/")

    yield driver

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
