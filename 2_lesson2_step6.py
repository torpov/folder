from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #1.Открыть страницу
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #2.Считать значение для переменной
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    
    #3.Посчитать математическую функцию от x.
    result = calc(x)
    
    #4.Проскроллить страницу вниз   
    browser.execute_script("window.scrollBy(0, 110);")
    
    #5.Ввести ответ в текстовое поле
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(result)
    
    #6.Выбрать checkbox "I'm the robot"
    browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    
    #7.Переключить radiobutton "Robots rule!"
    browser.find_element_by_xpath("//input[@id='robotsRule']").click()
    
    #8.Нажать на кнопку "Submit"
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
   
    
    

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()