# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import pickle

URL = 'http://vm-as444/?oid=1026366'

browser = webdriver.Chrome()
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
    time.sleep(2)
    if browser.find_element_by_xpath("//div[@data-id='" + i + "']").is_displayed:

         elem = browser.find_element_by_xpath("//div[@data-id='" + i + "']")
         ac = ActionChains(browser)
         ac.move_to_element_with_offset(elem, 1, 1).click().perform()
         ac.move_to_element_with_offset(elem, 1, 1).click().perform()
         time.sleep(1)
    try:
         if browser.find_element_by_xpath('//div[@class="qd-navigator-item"]').is_displayed:
             print(1111)
             for k in browser.finds_element_by_xpath('//div[@class="qd-navigator-item"]'):
                 k = k.get_attribute('data-index')
                 print(k, '@@@')
                 browser.find_element_by_xpath("//div[@data-index='" + k + "']").click()
#                 time.sleep(2)
#                 print('555')
#                 if int(k) == False:
#                     print('$$$$$$$$$$$$')
#                 print(777)
    except:
         pass
#    ff = []