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
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    browser.find_element_by_xpath("//button[@id='book']").click()
    
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    y = calc(x)
    
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
    button = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "solve")))
    button.click()
    
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()