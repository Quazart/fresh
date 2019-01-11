# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pickle

URL = 'http://vm-as444/?oid=1026084'

browser = webdriver.Chrome('D:\Anconda\envs\фрешдок\chromedriver.exe')
browser.get(URL)
cookies = pickle.load(open("cookies_freshdoc.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
browser.get(URL)
time.sleep(3)
browser.find_element_by_xpath("""//button[@title='Нажмите, чтобы перейти в режим "Правка"']""").click()
time.sleep(3)

soup = BeautifulSoup(browser.page_source, 'lxml')

count = 0
for i in soup.findAll('div', 'paragraph'):
    i = (i['data-id'])
    time.sleep(1)
    if browser.find_element_by_xpath("//div[@data-id='" + i + "']").is_displayed:
        try:
             elem = browser.find_element_by_xpath("//div[@data-id='" + i + "']")
             ac = ActionChains(browser)
             ac.move_to_element_with_offset(elem, 1, 1).click().perform()
             ac.move_to_element_with_offset(elem, 1, 1).click().perform()
#             browser.find_element_by_xpath("//div[@data-id='" + i + "']").send_keys(Keys.BACKSPACE)
#             browser.find_element_by_xpath("//div[@data-id='" + i + "']").send_keys(Keys.BACKSPACE)
#             browser.find_element_by_xpath("//div[@data-id='" + i + "']").send_keys(Keys.BACKSPACE)
             browser.find_element_by_xpath("//div[@data-id='" + i + "']").send_keys(Keys.SPACE)
             time.sleep(0.7)
             browser.find_element_by_xpath("//div[@data-id='" + i + "']").send_keys(Keys.CONTROL, 'a')
             time.sleep(0.5)
             browser.find_element_by_xpath('//button[@class="DD-button DD-button__action-target DD-minified"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//span[contains(@class, "qd-control-menuitem-caption") and text() = "Times New Roman"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//button[@title="Размер шрифта"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//span[contains(@class, "qd-control-menuitem-caption") and text() = "12"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//button[@title="Межстрочный интервал"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//span[contains(@class, "qd-control-menuitem-caption") and text() = "1"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//button[@title="Отступ первой строки"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//span[contains(@class, "qd-control-menuitem-caption") and text() = "1.0"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//button[@title="Цвет"]').click()
             time.sleep(0.5)
             browser.find_element_by_xpath('//span[@style = "background-color: rgb(0, 0, 0);"]').click()
#             time.sleep(0.5)
#             browser.find_element_by_xpath('//button[@title="Сохранить"]').click()
#             time.sleep(0.5)
#             browser.find_element_by_class_name('qd-control-menuitem-caption').click()
        except:
            pass
        count = count + 1
        print(count)
        if count == 15:
            time.sleep(0.5)
            browser.find_element_by_xpath('//button[@title="Сохранить"]').click()
            time.sleep(0.5)
            browser.find_element_by_class_name('qd-control-menuitem-caption').click()
            count = 0
