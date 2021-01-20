# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:18:17 2020

@author: Samresh
Saving all quots
"""
import requests
from bs4 import BeautifulSoup
import xlwt
import time 
from selenium.common.exceptions import NoSuchElementException

workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("quote-Data") 
  
# Specifying style 
style = xlwt.easyxf('font: bold 1') 
  
# Specifying column 
sheet.write(0, 0, 'Quote', style) 
sheet.write(0, 1, 'Author', style) 


all_quots = []
num = 1

def formate_quote(string):
    result = str(string).split('―')
    return result[0] + result[1]

while num in range(1,100):
    
    if num == 1:
        URL = 'https://www.goodreads.com/quotes'
    else:
        URL = f'https://www.goodreads.com/quotes?page={num}'
        
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_quots.extend(soup.find_all("div", class_="quoteText"))
    num+=1
    
count = len(all_quots)
print(f'quosts count are {count}')

for i in range(count):
        
        try:
            #msg = formate_quote(all_quots[i].text)
            result = str(all_quots[i].text).split('―')
            sheet.write(i+1, 0, result[0], style) 
            sheet.write(i+1, 1, result[1], style) 
            
        except NoSuchElementException:
            
            print('NoSuchElementException')
            
        time.sleep(.200)
        
workbook.save("sample.xls") 



