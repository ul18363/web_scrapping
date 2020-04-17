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
    
#Addiding index here also work (originally wasn't there
)
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
#%%
# url = "https://www.pythonforbeginners.com"
def iterative_expansion(soup_object,i=0,deep_limit=None):
    """
    Gets a soup object

    Parameters
    ----------
    i : TYPE, optional
        DESCRIPTION. The default is 0.
    deep_limit : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """
    
    if deep_limit:
        if i>deep_limit:
            return['Out of scope, recusrion is too deep!']
    
    children=list(soup_object.children)
    
    return children
#%%
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
    elem_list=ma.element_list(root)
    tree_dict=ma.element_tree_to_dict(root)
    ele_df=pd.DataFrame(elem_list)
    # Nelemen=0
    # tags=[]
    
    # for element in root.iter():
    #    print(element.tag)
    #    Nelemen+=1