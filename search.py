from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import pandas as pd
import numpy as np

temp = np.arange(9).reshape(1,9)
df = pd.DataFrame(temp)

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(3)

browser.get("http://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx")
Dept = browser.find_element_by_id("ddlKita")
Dept.send_keys("핵심교양")
results = browser.find_elements_by_class_name('Center')

my_course = []
count = 1
row = 0
for result in results:
    if count % 10 == 0:
        count = 1
        row +=1
        continue
    df.loc[row,[count-1]] = str(result.text)
    count += 1
df.to_csv("test.csv",mode='w',encoding='UTF-8')
