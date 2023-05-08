from selenium.webdriver import Chrome, Keys
import  time

def testHomework():
    driver = Chrome('lesson22/Homework18_Trofimenko/driver/chromedriver.exe')
    driver.get('http://google.com')

    search_input_field_locator = '//textarea[ @ type="search"]'
    first_search_link_locator = "//h3[contains(text(), 'MAKEUP - косметика и парфюмерия в интернет-магазине ...')]/.."
    sales_locator = "/html/body/div[1]/div[1]/header/div[1]/div/div[2]/ul/li[1]/a"
    sale_parfum_locator = "/html/body/div[1]/div[1]/nav/div[2]/ul[1]/li[3]/a"
    search_parfum_locator = '//div [@ data-popup-handler="search"]'
    input_search_locator = '//*[@id="search-input"]'

    search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    search_input_field.send_keys('Make up')
    search_input_field.send_keys(Keys.ENTER)
    time.sleep(2)
    first_search_link = driver.find_element(by='xpath', value=first_search_link_locator)
    first_search_link.click()
    time.sleep(2)
    sales = driver.find_element(by='xpath', value=sales_locator)
    sales.click()
    sale_parfum = driver.find_element(by='xpath', value=sale_parfum_locator)
    sale_parfum.click()
    time.sleep(2)
    search_parfum = driver.find_element(by='xpath', value=search_parfum_locator)
    search_parfum.click()
    input_search = driver.find_element(by='xpath', value=input_search_locator)
    input_search.send_keys('Versace')
    input_search.send_keys(Keys.ENTER)
    time.sleep(2)


    driver.quit()



