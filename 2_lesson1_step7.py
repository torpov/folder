from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    image_element = browser.find_element_by_xpath("//img[@id='treasure']")
    image_element_valuex = image_element.get_attribute("valuex")
    y = calc(image_element_valuex) 
    
    TF_answer = browser.find_element_by_xpath("//input[@id='answer']")
    TF_answer.send_keys(y)
    
    CHBrobot = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    CHBrobot.click()
    
    RBrule = browser.find_element_by_xpath("//input[@id='robotsRule']")
    RBrule.click()
    
    button = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    button.click()
    
    
    
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()