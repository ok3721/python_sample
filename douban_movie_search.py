import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import sys
import time


# class Logger(object):
#     def __init__(self, filename="Default.log"):
#         self.terminal = sys.stdout
#         self.log = open(filename, "a")
#
#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)
#
#     def flush(self):
#         pass
#
#
# sys.stdout = Logger('dianshi1.txt')

filmnames = ["飞刀问情", "红狐", "蓝盾"]
# filmnames = ["将军日记"]

# with open('dianshi1d799.csv', newline='') as f:
#     reader = csv.reader(f)
#     filmnames = list(reader)


for filmname in filmnames:
    print('------------------')

    print("Results for: ")
    print(filmname)
    s = Service("/usr/lib/chromium-browser/chromedriver")
    browser = webdriver.Chrome(service=s)

    browser.get("https://movie.douban.com/")
    search = browser.find_element(By.NAME, "search_text")
    search.send_keys(filmname)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    # titles = browser.find_elements(By.CLASS_NAME, "title-text")
    #
    # ratings = browser.find_elements(By.CLASS_NAME, "rating_nums")
    #
    # metas = browser.find_elements(By.CLASS_NAME, "meta.abstract_2")

    print([title.text for title in browser.find_elements(By.CLASS_NAME, "title-text")][:4])
    print([rating.text for rating in browser.find_elements(By.CLASS_NAME, "rating_nums")][:4])
    print([pl.text for pl in browser.find_elements(By.CLASS_NAME, "pl")][:4])
    print([meta.text for meta in browser.find_elements(By.CLASS_NAME, "meta.abstract_2")][:4])



    browser.quit()
    time.sleep(1 + random.random() * 3)
