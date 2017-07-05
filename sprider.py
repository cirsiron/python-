#encoding='utf8' 
from bs4 import BeautifulSoup
import requests
import json
import xlwt  
import re
import random
import time

workbook = xlwt.Workbook(encoding='utf-8')

def getMouthWeather(newUrl, dataid, booksheet):
    result = []
    res = requests.get(newUrl)
    soup = BeautifulSoup(res.text, 'html.parser')
    weather = soup.select('#tool_site .tqtongji2 ul')
    id = 0
    for lis in weather:
        obj = {}
        resli = lis.select("li")
        obj['id'] = id = id + 1
        obj['dates'] = resli[0].text
        obj['topTemp'] = resli[1].text
        obj['upTemp'] = resli[2].text
        obj['weather'] = resli[3].text
        obj['cloud'] = resli[4].text
        obj['cloudMax'] = resli[5].text
        result.append(obj)
    for i,row in enumerate(result):  
        for j,col in enumerate(row):  
            booksheet.write(i,j,row[col])  
    

def getWeather(url, year):
    for i in range(1, 13):
        if i<10:
            i = "0"+ str(i)
        newUrl =  'http://lishi.tianqi.com/hangzhou/' + str(year) + str(i) + '.html'
        print(newUrl)
        booksheet = workbook.add_sheet('杭州天气'+ str(year) +str(i) + "月", cell_overwrite_ok=True) 
        
        dateid = re.search('hangzhou/(.+).html', newUrl).group(1)
        getMouthWeather(newUrl, dateid, booksheet)

def getWeatherByYear():
    for i in range(2011, 2017):
        newYearUrl = 'http://lishi.tianqi.com/hangzhou/' + str(i) + '.html'
        getWeather(newYearUrl, i)
        workbook.save('杭州天气'+ str(i) +'.xls')
getWeatherByYear()











