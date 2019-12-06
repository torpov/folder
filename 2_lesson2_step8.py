from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #1.Открыть страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #2.Заполнить текстовые поля: имя, фамилия, email
    browser.find_element_by_xpath("//input[@name = 'firstname']").send_keys("Evgeny")
    browser.find_element_by_xpath("//input[@name = 'lastname']").send_keys("T")
    browser.find_element_by_xpath("//input[@name = 'email']").send_keys("123@mail.ru")
    
    #через цикл
    #for inp in browser.find_elements_by_css_selector(".form-group input"):
    #    inp.send_keys("data")
    
    #3.Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    element =  browser.find_element_by_xpath("//input[@id = 'file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    
    #4.Нажать кнопку "Submit"   
    browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
   
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()