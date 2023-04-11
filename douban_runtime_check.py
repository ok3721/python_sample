from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import random
import logging
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # options.add_experimental_option("excludeSwitches", ["enable-logging","enable automation"])
        # options.add_argument(row1["profile_directory"])
        # options.add_argument("user-data-dir=C:\\Users\\AOSS\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome(options=options)

file = 'C:/Users/AOSS/Desktop/新建文件夹/22/408.xlsx'
xl = pd.ExcelFile(file)
df1 = xl.parse('Sheet1')
# print(df1)
i = 0

for index, row in df1.iterrows():
    try:
        if "douban" not in row["douban"]:
            print(str(i)+" "+ row["filmname"]+" nan!!")
            df1.loc[index, 'runtime'] = "no time!"    
            i+=1
        
        else:
            driver.get(row["douban"])
            WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/h1/span[1]')))
            name = driver.find_element(By.XPATH,'//*[@id="content"]/h1/span[1]').text
            runb = driver.find_elements(By.XPATH,'//*[@id="info"]/span[@property="v:runtime"]')
            if len(runb) == 0:
                print(str(i)+ row["filmname"]+" no time!")
                df1.loc[index, 'runtime'] = "no time!"
            else:
                runtime = runb[0].text
                print(str(i)+" "+ name +"time: "+ runtime)
                df1.loc[index, 'runtime'] = runtime
                df1.loc[index, 'doubanname'] = name
                
        
            i += 1
            
            time.sleep(6 + random.random() * random.random())
    except Exception as e:
        print("Error")
        print(e)
        df1.loc[index, 'runtime'] = e
        print(df1)
        df1.to_excel('C:/Users/AOSS/Desktop/新建文件夹/22/4043.xlsx', sheet_name='Sheet2', index= False)


print("all ok")
print(df1)
df1.to_excel('C:/Users/AOSS/Desktop/新建文件夹/22/4043.xlsx', sheet_name='Sheet1', index= False)
