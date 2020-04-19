# -*- coding: utf-8 -*-
# External libraries to add
import pandas as pd
import os
import json
import landbay.xml_processing.xsd_analyzer as analyzer
import landbay.xml_processing.markup_analyzer as ma
import numpy as np
from requests_html import HTMLSession
import sys

#Internal libraries to add
personal_libary_path= '/media/bruno/Extra/Ubuntu-Repository/personal_library/'
landbay_libary_path='/media/bruno/Extra/Ubuntu-Repository/landbay_repo/landbay_local'
if not landbay_libary_path in sys.path:
    sys.path.insert(0,landbay_libary_path)
if not personal_libary_path in sys.path:
    sys.path.insert(0,personal_libary_path)
del landbay_libary_path 
del personal_libary_path

class rightmove_handler():
    
    def __init__(self,driver=None): 
        super(rightmove_handler, self).__init__()
        self.driver=driver
        self.location_prefix='OUTCODE%5E'
        self.elems_per_page=24
        self.development_mode=True
        self.outer_zones=random.shuffle(list(range(1,2921+1))) #By shuffling the zones perhaps the pattern is harder to detect
        self.session=None
        
    def generate_session(self,proxy=None):
        self.session=HTMLSession()
        if proxy:
            self.session.proxies.update({'http': 'http://'+proxy_address,'https': 'https://'+proxy_address})
        return 0
    
    def get_all_houses_for_sale(self):
        zones=self.get_range_of_zones()
        results={}
        for zone in zones:
            results[zone]=self.search_zone_purchase(zone)
        return None
    
    def get_number_of_results(data):
        return int(data['resultCount'])
    
    def get_request(self,url,param_tuple):
        parameters = urllib.parse.urlencode(param_tuples)
        get_url = url + parameters
    
    def search_zone_purchase(self,zone_id):
        url='https://www.rightmove.co.uk/property-for-sale/find.html?'
        param_tuple=[('index','0'),('locationIdentifier',self.location_prefix+str(zone_id))]
        
    def get_range_of_zones(self):
        return list(range(1,2921))
        
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
        start_ix=html_body.find(trigger)
        if start_ix==-1:
            print('Trigger block text ['+trigger+'] couldnt be found! Returning None')
            f=open('error_page_rightmove.html','a')
            f.write(html_body)
            f.close()
                raise ValueError
            return None
        start_ix=start_ix+len(trigger)-1
        
        c_d={'{':1,'}':-1}
        skip_val='"'
        balance=0
        ix=start_ix
        balance_achieved=False
        while not balance_achieved:
            char=html_body[ix]
            if char == "{" or char =="}":
                balance=balance+c_d[char]
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
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    url='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
    url_search='https://www.rightmove.co.uk/property-for-sale/search.html?searchLocation=SW1P&useLocationIdentifier=true&locationIdentifier=OUTCODE%5E2509&buy.x=SALE&search=Start+Search'
    url_find='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=2&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'
    
    handler=rightmove_handler()
    html_body= open('outcome/rightmove_sample_find.html','r').read()
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
