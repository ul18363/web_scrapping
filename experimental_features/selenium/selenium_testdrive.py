# -*- coding: utf-8 -*-
"""
https://www.freecodecamp.org/news/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251/

One may need to get chrome-driver first:
    sudo apt install chromium-chromedriver
    
    or if compatibility issues show up follow:
    https://makandracards.com/makandra/29465-install-chromedriver-on-linux
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)
#%%
python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_0') #FHSU
python_button.click() #click fhsu link


#%%
dict_xy=driver.get_window_position()
driver.set_window_position(x=2400, y=300)

url_find='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=2&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'

driver.get(url_find)
#%% Close driver 
# driver.close()