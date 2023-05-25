import time


def test_check_choose_category(dashboard):
    dashboard.click_on_sale()
    pick_subcategory = dashboard.choose_subcategory('Акції')
    sale_subcat = pick_subcategory.choose_perfumes_selection()
    time.sleep(5)

def test_check_login(dashboard):
    login = dashboard.login_form()
    login.fill_row('elizzar1987@gmail.com', 'liza1987')
    time.sleep(5)

def test_get_cookies(cookies, driver):
    our_cookies = cookies.get_cookies(driver)
    print(our_cookies)
    time.sleep(5)

def test_set_local_storage(local_storage, driver):
    setting_local_storage = local_storage.set_local_storage(driver)
    print(driver.execute_script("return window.localStorage['test']; "))