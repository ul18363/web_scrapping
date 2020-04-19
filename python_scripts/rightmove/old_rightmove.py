# -*- coding: utf-8 -*-
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
#%%
# url = "https://www.pythonforbeginners.com"

def extract_data(html_body):
    trigger='window.jsonModel = {'
    start_ix=txt.find(trigger)+len(trigger)-1
    c_d={'{':1,'}':-1}
#    skip_val='"'
    balance=0
    ix=start_ix
#    ix=start_ix+len(trigger)-1
    balance_achieved=False
    while not balance_achieved:
        char=html_body[ix]
        if char == "{" or char =="}":
#            print(ix)
            balance=balance+c_d[char]
            print(char+':'+str(ix)+' | '+str(balance))
#        if char==skip_val:
#            ix=txt.find(skip_val,ix+1)
        if balance==0:
            balance_achieved=True
            break
        ix=ix+1
    end_ix=ix+1
#    txt2=txt[start_ix:end_ix]
    data=json.loads(txt[start_ix:end_ix])
    return data

class rightmove_handler():
    
    def __init__(self,driver=None): 
        super(rightmove_handler, self).__init__()
        self.driver=driver
        self.outer_zones=random.shuffle(list(range(1,2921+1))) #By shuffling the zones perhaps the pattern is harder to detect
        
    def search_zone_purchase(self,params_tuple=[]):
        url='https://www.rightmove.co.uk/property-for-sale/find.html?'
        
    def search_zone_rent(self,params_tuple=[]):
        url='https://www.rightmove.co.uk/property-to-rent/find.html?'
        
def proxy_request(request_type,url,**kwargs):
    while True:
        proxy=get_proxy()
       
        try: 
            print("Using proxy: {}".format(proxy))
            r= requests.request(request_type,url,proxies=proxy,timeout=5,**kwargs)
            break
        except:
            print("Failed to use proxy: {}".format(proxy))
            pass
    return r



if __name__=='__main__':
    

    #%%
    url='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
    url_search='https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=SW1P&useLocationIdentifier=true&locationIdentifier=OUTCODE%5E2509&buy.x=SALE&search=Start+Search'
    url_find='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=2&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'

    # http = urllib.PoolManager()
    # response = http.request('GET', url_find)
    # content = response.data
    # soup = BeautifulSoup(content)
    
    # y=iterative_expansion(soup)
    # create a new Firefox session
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    txt=driver.page_source
    # lxml.html.fromstring(txt)
    parser = etree.HTMLParser()
    tree   = etree.parse(StringIO(txt), parser)
    root=tree.getroot()
    tag=root.tag
    childs=root.getchildren()
    all_keys=dir(root)
    atr_keys=[x for x in all_keys if not x.startswith('__')]
    callable_keys=[x for x in atr_keys if callable(root.__getattribute__(x))]
    non_callable_keys=[x for x in atr_keys if not callable(root.__getattribute__(x))]
    file_name='rightmove_sample_find.html'
    xsd_file_name='schema_euroabs.xsd'
    # root = etree.fromstring(xml)
    anz=ma.MarkUpAnalyzer(language='html')
    tree_dict=ma.element_tree_to_dict(root)
    elem_list=ma.element_list(root)
    ele_df=pd.DataFrame(elem_list)
    ele_df_js=ele_df[ele_df['tag']=='script']
    script=ele_df_js['element'].iat[0]
    scripts=[x.attrib for x in ele_df_js['element']]
    scripts_df=pd.DataFrame(scripts)
    #%%

    data=extract_data(txt)
    #houses per page
    elems_per_page=24
    properties_df=pd.DataFrame(data['properties'])
    properties_shown=data['maxCardsPerPage']
#    search_params_df=pd.DataFrame(data['searchParameters'],index=[0])
    search_params=data['searchParameters']
    location_df=data['location']
    location_df=pd.DataFrame(data['location'],index=[0])
    resultCount=data['resultCount']
    n_searches=int(np.floor(resultCount/elems_per_page))
    n_searches=range(n_searches+1)
    n_searches=[x*elems_per_page for x in n_searches]
    
    

    
    # Nelemen=0
    # tags=[]
    
    # for element in root.iter():
    #    print(element.tag)
    #    Nelemen+=1