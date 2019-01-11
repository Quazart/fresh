# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pickle

URL = 'http://vm-as444/?oid=1027492'

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


elem = browser.find_element_by_xpath("//div[@data-id='eKNZ8A69Y-0']")
ac = ActionChains(browser)
ac.move_to_element_with_offset(elem, 1, 1).click().perform()
ac.move_to_element_with_offset(elem, 1, 1).click().perform()
time.sleep(1)
for i in soup.findAll('div', class_='qd-navigator-item'):
    print(i)
if browser.find_element_by_xpath('//div[@class="qd-navigator-item"]').is_displayed():
    for i in browser.find_elements_by_xpath('//div[@class="qd-navigator-item"]'):
        i = i.get_attribute('data-index')
        print(i)
        browser.find_element_by_xpath("//div[@data-index='" + i + "']").click()
