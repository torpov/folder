from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #1.Открыть страницу
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    # неявное ожидание в течении 5 секунд
    browser.implicitly_wait(5) 
    browser.get(link)
    #time.sleep(2)
    
    #2.Нажать на кнопку "Verify"
    browser.find_element_by_xpath("//button[@id = 'verify']").click()
    #time.sleep(1)
    
    #3.Проверить, что появилась надпись "Verification was successful!"  
    assert "successful" in browser.find_element_by_xpath("//div[@id = 'verify_message']").text
    
   
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()