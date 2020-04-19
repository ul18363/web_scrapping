# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,'/media/bruno/Extra/Ubuntu-Repository/landbay_repo/landbay_local')
"""

https://www.rightmove.co.uk/property-for-sale/search.html?
    searchLocation=SW1P&
    useLocationIdentifier=false&
    locationIdentifier=&
    radius=0.0&
    displayPropertyType=&
    minBedrooms=&
    minPrice=&
    maxPrice=&
    maxDaysSinceAdded=&
    buy.x=SALE&
    search=Start+Search

radius=0.25 #is for quarter mile options= [0.0,0.25,0.5,1,3,5,10,15,20,30,40]

https://www.rightmove.co.uk/property-for-sale/find.html?
    searchType=SALE&
    locationIdentifier=OUTCODE%5E2509&
    insId=2&
    radius=0.0&
    minPrice=&
    maxPrice=&
    minBedrooms=&
    maxBedrooms=&
    displayPropertyType=&
    maxDaysSinceAdded=&
    _includeSSTC=on&
    sortByPriceDescending=&
    primaryDisplayPropertyType=&
    secondaryDisplayPropertyType=&
    oldDisplayPropertyType=&
    oldPrimaryDisplayPropertyType=&
    newHome=&
    index=24&
    auction=false
    
#Addiding index here also work (originally wasn't there)
    If index is greater than the number of results the value is ommited in the search (aka index is set to 0)
    If index is +-12 places from i*24 page i will appear
# locationIdentifier: Amazingly the outer postcode area is represented by a number 1 or bigger.
    AB10 ->1
    AB10 1AF -> 000001
    AB11 ->2
    SW1P -> 2509
    SW1P 2NR ->837742
 # Probably ZE3->2921 is the last one

https://www.rightmove.co.uk/property-for-sale/find.html?
    locationIdentifier=OUTCODE%5E2509&
    index=24&
    propertyTypes=&
    includeSSTC=false&
    mustHave=&
    dontShow=&
    furnishTypes=&
    keywords=
    
    
renturl:
    https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=OUTCODE%5E2509&sortType=1&propertyTypes=&includeLetAgreed=false&mustHave=&dontShow=&furnishTypes=&keywords=
can be WAAAY simplified!
https://www.rightmove.co.uk/property-to-rent/find.html?index=0&locationIdentifier=OUTCODE%5E18
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import json
import lxml
from io import StringIO, BytesIO
import sys

if not '/media/bruno/Extra/Ubuntu-Repository/landbay_repo/landbay_local' in sys.path:
    sys.path.insert(0,'/media/bruno/Extra/Ubuntu-Repository/landbay_repo/landbay_local')
import landbay.xml_processing.xsd_analyzer as analyzer
import landbay.xml_processing.markup_analyzer as ma

from bs4 import BeautifulSoup
import urllib3 as urllib
from lxml import etree
import numpy as np
import random

class rightmove_handler():
    
    def __init__(self,driver=None): 
        super(rightmove_handler, self).__init__()
        self.driver=driver
        self.location_prefix='OUTCODE%5E'
        self.elems_per_page=24
        self.outer_zones=random.shuffle(list(range(1,2921+1))) #By shuffling the zones perhaps the pattern is harder to detect
        
    def search_zone_purchase(self,params_tuple=[]):
        url='https://www.rightmove.co.uk/property-for-sale/find.html?'
        param_tuple=[('index','0'),]
        
    def search_zone_rent(self,params_tuple=[]):
        url='https://www.rightmove.co.uk/property-to-rent/find.html?'
    
    def get_url_param_tuple_example(url):
        """
            Retrieve tuple for some base url, the main point is to have 
            the parameters at hand if they come handy in the future.
        """
        tup=[]
        if url=='https://www.rightmove.co.uk/property-for-sale/find.html?':
            tup=[('searchType','SALE'),
                 ('locationIdentifier','OUTCODE%5E2509'),
                 ('insId',2),
                 ('radius',0.0),
                 ('minPrice',''),
                 ('maxPrice',''),
                 ('minBedrooms',''),
                 ('maxBedrooms',''),
                 ('displayPropertyType',''),
                 ('maxDaysSinceAdded',''),
                 ('_includeSSTC','on'),
                 ('sortByPriceDescending',''),
                 ('primaryDisplayPropertyType',''),
                 ('secondaryDisplayPropertyType',''),
                 ('oldDisplayPropertyType',''),
                 ('oldPrimaryDisplayPropertyType',''),
                 ('newHome',''),
                 ('index',24),
                 ('auction',False)]
        elif url=='https://www.rightmove.co.uk/property-for-sale/search.html?':
            tup=[('searchLocation','SW1P')
                 ('useLocationIdentifier','false')
                 ('locationIdentifier','')
                 ('radius','0.0')
                 ('displayPropertyType','')
                 ('minBedrooms','')
                 ('minPrice','')
                 ('maxPrice','')
                 ('maxDaysSinceAdded','')
                 ('buy.x','SALE')
                 ('search','Start+Search')]
        elif url=='https://www.rightmove.co.uk/property-to-rent/find.html?':
            tup=[('locationIdentifier','OUTCODE%5E2509'),
                 ('propertyTypes',''),
                 ('mustHave',''),
                 ('dontShow',''),
                 ('furnishTypes',''),
                 ('keywords',''),
                 ('index','24')]
        return tup

    def extract_data_from_page_source(self,html_body, formatting='JSON'):
        """
        
        """
        trigger='window.jsonModel = {'
        start_ix=html_body.find(trigger)+len(trigger)-1
        c_d={'{':1,'}':-1}
        skip_val='"'
        balance=0
        ix=start_ix
#        ix=start_ix+len(trigger)-1
        balance_achieved=False
        while not balance_achieved:
            char=html_body[ix]
            if char == "{" or char =="}":
                balance=balance+c_d[char]
#                print(char+':'+str(ix)+' | '+str(balance))
            if char==skip_val:
                ix=html_body.find(skip_val,ix+1)
            if balance==0:
                balance_achieved=True
                break
            ix=ix+1
        end_ix=ix+1
        
        if formatting=='JSON':
            data=json.loads(html_body[start_ix:end_ix])
            return data
        else:
            print('Please choose from JSON, DataFrame')
            return locals()#html_body[start_ix:end_ix]

if __name__=='__main__':
#    import os
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    #%%
    url='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
    url_search='https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=SW1P&useLocationIdentifier=true&locationIdentifier=OUTCODE%5E2509&buy.x=SALE&search=Start+Search'
    url_find='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=2&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
    
    handler=rightmove_handler()
    html_body= open('rightmove_sample_find.html','r').read()
    data=handler.extract_data_from_page_source(html_body,formatting='JSON')
#    #houses per page
#    elems_per_page=24
#    properties_df=pd.DataFrame(data['properties'])
#    properties_shown=data['maxCardsPerPage']
##    search_params_df=pd.DataFrame(data['searchParameters'],index=[0])
#    search_params=data['searchParameters']
#    location_df=data['location']
#    location_df=pd.DataFrame(data['location'],index=[0])
#    resultCount=data['resultCount']
#    n_searches=int(np.floor(resultCount/elems_per_page))
#    n_searches=range(n_searches+1)
#    n_searches=[x*elems_per_page for x in n_searches]
