from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    # browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait2.html")

    # button = browser.find_element_by_id("verify")
    
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    button.click()
    
    message = browser.find_element_by_id("verify_message")
 
    assert "successful" in message.text
 
   
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()