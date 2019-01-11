# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pickle

URL = 'http://vm-as444/?oid=1026435'

browser = webdriver.Chrome('D:\Anconda\envs\фрешдок\chromedriver.exe')
browser.get(URL)
time.sleep(30)

pickle.dump(browser.get_cookies(), open('cookies_freshdoc.pkl', 'wb'))
