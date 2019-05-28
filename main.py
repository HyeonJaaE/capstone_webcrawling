from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import pandas as pd
import numpy as np
import csv

temp = np.arange(9).reshape(1,9)
df = pd.DataFrame(temp)


dept = [
"기계공학과 / 기계공학",
"항공우주공학과 / 항공우주공학",
"조선해양공학과 / 조선해양공학",
"산업경영공학과 / 산업경영공학",
"화학공학과 / 화학공학",
"생명공학과 / 생명공학",
"고분자공학과 / 고분자공학",
"신소재공학과 / 신소재공학",
"사회인프라공학과 / 사회인프라공학",
"컴퓨터공학과 / 컴퓨터공학"]

for d in dept:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(3)
    browser.get("http://sugang.inha.ac.kr/sugang/SU_51001/Lec_Time_Search.aspx")
    Dept = browser.find_element_by_id("ddlDept")
    Dept.send_keys(d)
    browser.find_element_by_id("ibtnSearch1").click()
    results = browser.find_elements_by_class_name('Center')

    #기계공학과 / 기계공학
    #항공우주공학과 / 항공우주공학
    #조선해양공학과 / 조선해양공학
    #산업경영공학과 / 산업경영공학
    #화학공학과 / 화학공학
    #생명공학과 / 생명공학
    #고분자공학과 / 고분자공학
    #신소재공학과 / 신소재공학
    #사회인프라공학과 / 사회인프라공학
    #컴퓨터공학과 / 컴퓨터공학

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


    fr = open('test.csv', 'r', encoding='utf-8')
    tmp = list(csv.reader(fr))

    rdr = tmp[1:]
    fr.close()

    tmpd = d.split(" ")
    filename = tmpd[0] + ".csv"
    fw = open(filename, 'w', encoding='utf-8', newline='')
    wr = csv.writer(fw)

    check = ['월','화','수','목','금']
    for line in rdr:
        day = ""
        time = ""
        room = ""

        if line[7] == " ":
            continue

        a = line[7].split('/')
        sum = ""
        for b in a:
            c = b.split('(', maxsplit=1)
            room += c[1].replace(")", "")
            sum += c[0]

        sum = sum.replace(",","")
        sumList = list(sum)

        day += sumList[0]
        time += sumList[1]

        for i in range(2, len(sumList)):
            if sumList[i] in check:
                day += ("-" + sumList[i])
                time += ("_" + sumList[i-1])
                time += ("-" + sumList[i+1])
            if i == len(sumList)-1:
                time += ("_" + sumList[i])

        tmp = [line[1], line[3], line[4], int(float(line[5])),line[6], line[9], day, time, room, line[8]]
        wr.writerow(tmp)

    fw.close()
