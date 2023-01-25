import random
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import sys
import time

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger('dianshiju1.txt')


# urls = ["https://movie.douban.com/subject/5385051/", "https://movie.douban.com/subject/4811774/", "https://movie.douban.com/subject/1652587/", "https://movie.douban.com/subject/5348089/"]
# filmnames = ["将军日记"]

# file = 'list2.xlsx'
# xl = pandas.ExcelFile(file)
# df1 = xl.parse('Sheet1')
#
# urls = list(df1.name)


with open('24.csv', 'r') as csv_file:

    urls = csv.reader(csv_file)

    for url in urls:
        print('------------------')
        print("Results for: ")
        print(url)
        s = Service("/usr/lib/chromium-browser/chromedriver")
        browser = webdriver.Chrome(service=s)

        browser.get(url[0])
        time.sleep(2 + random.random() * 3)
        title = browser.find_element(By.XPATH, "/html/body/div[4]/div[3]/div[2]/div[1]")
        ff1 = "Name" + " " + title.text
        print(ff1)
        vname = browser.find_element(By.XPATH, "/html/body/div[5]/div[2]").text
        vlist = vname.split("\n")
        ff2 = "Nos" + " " + str(len(vlist))
        print(ff2)
