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
ttps://www.rightmove.co.uk/property-for-sale/find.html?
    locationIdentifier=OUTCODE%5E2509&
    index=24&
    propertyTypes=&
    includeSSTC=false&
    mustHave=&
    dontShow=&
    furnishTypes=&
    keywords=
"""


def base_search():
    
    
    return None

from bs4 import BeautifulSoup
import urllib3 as urllib

# url = "https://www.pythonforbeginners.com"

if __name__=='__main__':
    url='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=1&radius=0.25&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
    url_search='https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=SW1P&useLocationIdentifier=true&locationIdentifier=OUTCODE%5E2509&buy.x=SALE&search=Start+Search'
    url_find='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=2&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'

    http = urllib.PoolManager()
    response = http.request('GET', url_find)
    content = response.data
    soup = BeautifulSoup(content)