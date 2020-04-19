# -*- coding: utf-8 -*-

"""
    pip install requests-html
    
"""
from requests_html import HTMLSession
session = HTMLSession()
test_url='https://httpbin.org/ip'
url='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=2&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'

r = session.get(url)