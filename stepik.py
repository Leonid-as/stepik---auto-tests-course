from selenium import webdriver
import math


#Selenium Waits (Implicit Waits)
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text

import pdb
pdb.set_trace()





'''
#Selenium Waits (Implicit Waits)
browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("check")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text



___________________________________________


# переход на новую вкладку
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)


button = browser.find_element_by_tag_name("button").click()



browser.switch_to.window(browser.window_handles[1])
sleep(1)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
button = browser.find_element_by_tag_name("button").click()





____________________________________



# принимаем alert (всплывающее окно)
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_tag_name("button").click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id ('input_value')
x = x_element.text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)


button = browser.find_element_by_tag_name("button").click()


--------------------------------------------


# Задание на execute_script . Когда искомый элемент закрывает другой элемент. Нужно сделать скрол.
browser = webdriver.Chrome()
link = " http://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id ('input_value')
x = x_element.text
y = calc(x)

x_input = browser.find_element_by_id('answer')
x_input.send_keys(y)

check_1 = browser.find_element_by_id('robotCheckbox').click()

radio_1 = browser.find_element_by_id('robotsRule')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
radio_1.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
button.click()


--------------------------------------------




# Работа с выпадающим списком

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


num1 = browser.find_element_by_id('num1').text
num2 = browser.find_element_by_id('num2').text

summ = int(num1) + int(num2)

browser.find_element_by_id('dropdown').click()
browser.find_element_by_xpath(f'//select/option[@value="{summ}"]').click()


button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()


--------------------------------------------


#поиск сокровища с помощью get_attribute.значение переменной х спрятано в 
"сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


sunduk = browser.find_element_by_id('treasure')
x = sunduk.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

x_input = browser.find_element_by_id('answer')
x_input.send_keys(y)

Check_1 = browser.find_element_by_id('robotCheckbox')
Check_1.click()

Check_2 = browser.find_element_by_id('robotsRule')
Check_2.click()

button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()


--------------------------------------------


# вычислить формулу, вставить в поле и выбрать чекбокс и радиобатонн

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id ('input_value')
x = x_element.text
y = calc(x)

x_input = browser.find_element_by_id('answer')
x_input.send_keys(y)

Check_1 = browser.find_element_by_id('robotCheckbox')
Check_1.click()

Check_2 = browser.find_element_by_id('robotsRule')
Check_2.click()

button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()



--------------------------------------------


#Заполнить 30 форм

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)


link_2 = browser.find_element_by_name('control')
link_2.send_keys('Pizda')

link_3 = browser.find_element_by_name('e-mail')
link_3.send_keys('Pizda2')

link_4 = browser.find_element_by_name('lastname')
link_4.send_keys('Мой ответ')

link_5 = browser.find_element_by_name('firstname')
link_5.send_keys('Мой ответ')


elements = browser.find_elements_by_tag_name("input")
for element in (i for i in elements if i not in {link_2, link_4, link_3, link_5}):
    element.send_keys("Мой ответ")

sleep(100**3)

button = browser.find_element_by_css_selector("button.btn")
button.click()


--------------------------------------------



#Заполнить форму найти кнопку "Отправить" и нажать на неё

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name('input')
input1.send_keys('Ivaan')

input2 = browser.find_element_by_name('last_name')
input2.send_keys('Petrov')

input3 = browser.find_element_by_class_name('form-control.city')
input3.send_keys("Smolensk")

input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")

button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()



link_2 = browser.find_element_by_name('control')
ink_2.send_keys('Мой ответ')

link_3 = browser.find_element_by_name('e-mail')
link_3.send_keys('Мой ответ')

link_4 = browser.find_element_by_name('lastname')
link_4.send_keys('Мой ответ')

link_5 = browser.find_element_by_name('firstname')
link_5.send_keys('Мой ответ')


elements = browser.find_elements_by_tag_name("input")
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()

'''
