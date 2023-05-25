from selenium.webdriver import Chrome
from lesson_23.Homework20_Trofimenko.pages.dashboard_page import Dashboard

import pytest
import time

@pytest.fixture(scope="session")
def driver():
    driver = Chrome('lesson_25/Homework21_Trofimenko/drivers/chromedriver.exe')
    driver.get("https://makeup.com.ua/")

    yield driver

    print(driver.get_cookies())
    time.sleep(5)

    driver.quit()


@pytest.fixture
def dashboard(driver):
    yield Dashboard(driver)
