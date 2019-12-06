from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #1.Открыть страницу
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #2.Нажать на кнопку
    browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']").click()
    time.sleep(1)
    
    #3.Переключиться на новую вкладку
    new_window = browser.window_handles[1] 
    browser.switch_to.window(new_window)
    
    #4.Пройти капчу для робота и получить число-ответ   
    image_element = browser.find_element_by_xpath("//span[@id='input_value']").text
    y = calc(image_element)
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    
    
   
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()