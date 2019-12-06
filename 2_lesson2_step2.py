from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = int(browser.find_element_by_xpath("//span[@id = 'num1']").text)
    y = int(browser.find_element_by_xpath("//span[@id = 'num2']").text)
    summ = x + y
    
    select = Select(browser.find_element_by_xpath("//select[@id = 'dropdown']"))
    select.select_by_value(summ)
    
    button = browser.find_element_by_xpath("//button[@class = 'btn btn-default']").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()