import time


def test_check_choose_category(dashboard):
    dashboard.click_on_sale()
    dashboard.choose_sale_parfums('Парфумерия')
    time.sleep(5)