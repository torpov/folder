from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    valuex = browser.find_element_by_xpath("//span[@id = 'input_value']")
    x = valuex.text
    y = calc(x)
    
    answer = browser.find_element_by_xpath("//input[@id = 'answer']")
    answer.send_keys(y)
    
    checkbox = browser.find_element_by_xpath("//input[@id = 'robotCheckbox']")
    checkbox.click()
    
    robots = browser.find_element_by_xpath("//input[@id = 'robotsRule']")
    robots.click()
    
    button = browser.find_element_by_xpath("//button[@type = 'submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()