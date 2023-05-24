import time


def test_check_choose_category(dashboard):
    dashboard.click_on_sale()
    pick_subcategory = dashboard.choose_subcategory('Акції')
    sale_subcat = pick_subcategory.choose_perfumes_selection()
    time.sleep(5)

