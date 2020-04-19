# -*- coding: utf-8 -*-
# External libraries to add
import pandas as pd
import os
import json
import urllib
#import landbay.xml_processing.xsd_analyzer as analyzer
#import landbay.xml_processing.markup_analyzer as ma
import numpy as np
from requests_html import HTMLSession
import sys
import datetime
#from datetime.datetime import now 
#Internal libraries to add
personal_libary_path= '/media/bruno/Extra/Ubuntu-Repository/personal_library/'
landbay_libary_path='/media/bruno/Extra/Ubuntu-Repository/landbay_repo/landbay_local'
if not landbay_libary_path in sys.path:
    sys.path.insert(0,landbay_libary_path)
if not personal_libary_path in sys.path:
    sys.path.insert(0,personal_libary_path)
del landbay_libary_path 
del personal_libary_path

def now():
    return datetime.datetime.now()
def timestamp():
    return datetime.datetime.strftime(now(),"%Y_%m_%d_%H_%M_%S")
class rightmove_handler():
    
    def __init__(self,driver=None,proxy=None): 
        super(rightmove_handler, self).__init__()
        self.driver=driver
        self.enable_dump=True
#        self.default_dump_folder='outcome/'
        self.dump_folder='outcome/'
        self.location_prefix="OUTCODE%5E"
        self.elems_per_page=24
        self.development_mode=True
#        self.outer_zones=random.shuffle(list(range(1,2921+1))) #By shuffling the zones perhaps the pattern is harder to detect
        self.outer_zones=list(range(1,2921+1)) #By shuffling the zones perhaps the pattern is harder to detect
        self.generate_session(proxy=proxy)
        self.last_url=None
        self.last_response=None
        self.failed_list=[]
        
    def generate_session(self,proxy=None):
        self.session=HTMLSession()
        if proxy:
            self.session.proxies.update({'http': 'http://'+proxy,'https': 'https://'+proxy})
        return 0
    def update_dump_folder(self,prefix='',suffix='',create_folder=True):
        self.dump_folder=prefix+'outcome_'+timestamp()+suffix+'/'
        if create_folder:
            os.mkdir(self.dump_folder)
        return 0
    def parse_parameters(self,param_tuples, use_urllib=False):
        if use_urllib:
            parameters=urllib.parse.urlencode(param_tuples)         
        else:    
            parameters=[str(p[0])+'='+str(p[1]) for p in param_tuples]
            parameters='&'.join(parameters)
        return parameters
    
    def get_all_houses_for_sale(self,update_dump_folder=True):
        if update_dump_folder:
            self.update_dump_folder(suffix='_sale')
        zones=self.get_range_of_zones()
        results={}
        for zone in zones:
            try:
                results[zone]=self.search_zone_purchase(zone)
            except KeyboardInterrupt:
                # quit if ctrl c or something like that
                sys.exit()
            except: # Something went wrong what do we do? Just add it to the failed list and display a message
                print('locationIdentifier: '+str(zone)+'failed with status '+str(self.last_response.status_code))
                report={}
                report['response']=self.last_response
                report['Source']='get_all_houses_for_sale'
                self.failed_list.append(report)
                
        return results
    def get_all_houses_for_rent(self,update_dump_folder=True):
        if update_dump_folder:
            self.update_dump_folder(suffix='_rent')
        zones=self.get_range_of_zones()
        results={}
        for zone in zones:
            try:
                results[zone]=self.search_zone_rent(zone)
            except KeyboardInterrupt:
                # quit if ctrl c or something like that
                sys.exit()
            except: # Something went wrong what do we do? Just add it to the failed list and display a message
                print('locationIdentifier: '+str(zone)+'failed with status '+str(self.last_response.status_code))
                report={}
                report['response']=self.last_response
                report['Source']='get_all_houses_for_sale'
                self.failed_list.append(report)
                
        return results    
    def get_number_of_results(self,data):
        try:
            return int(data['resultCount'])
        except:
            return 0
        
    def get_rest_of_indexes(self,data):
        resultCount=self.get_number_of_results(data)
        elems_per_page=self.elems_per_page
        if resultCount<=elems_per_page:
            return []
        remaining_indexes=int(np.floor(resultCount/elems_per_page))
        remaining_indexes=range(1,remaining_indexes+1)
        remaining_indexes=[x*elems_per_page for x in remaining_indexes]
        return remaining_indexes
    
    def get_request(self,url,param_tuples):
        parameters = self.parse_parameters(param_tuples)
        get_url = url + parameters
        self.last_url=get_url
        r= self.session.request('get',get_url,timeout=5)
        self.last_response=r
        return r
    
    def search_zone_purchase(self,zone_id):
        results=[]
        url='https://www.rightmove.co.uk/property-for-sale/find.html?'
        loc_tuple=('locationIdentifier',self.location_prefix+str(zone_id))
        index_tuple=('index','0')
        param_tuples=[index_tuple,loc_tuple]
        r= self.get_request(url,param_tuples)
#        return r
        data= self.extract_data_from_page_source(r.text)
        results.append(data)
        remaining_indexes=self.get_rest_of_indexes(data)
        for index in remaining_indexes:
            index_tuple=('index',index)
            param_tuples=[index_tuple,loc_tuple]
            r= self.get_request(url,param_tuples)
            data= self.extract_data_from_page_source(r.text)
            results.append(data)
        if self.dump_folder:
            json.dump(results,open(self.dump_folder+str(zone_id)+'__'+timestamp()+'.json','a'))
        return result
    
   
    def get_range_of_zones(self):
        return list(range(1,2921))
        
    def search_zone_rent(self,zone_id):
        results=[]
        url='https://www.rightmove.co.uk/property-to-rent/find.html?'
        loc_tuple=('locationIdentifier',self.location_prefix+str(zone_id))
        index_tuple=('index','0')
        param_tuples=[index_tuple,loc_tuple]
        r= self.get_request(url,param_tuples)
#        return r
        data= self.extract_data_from_page_source(r.text)
        results.append(data)
        remaining_indexes=self.get_rest_of_indexes(data)
        for index in remaining_indexes:
            index_tuple=('index',index)
            param_tuples=[index_tuple,loc_tuple]
            r= self.get_request(url,param_tuples)
            data= self.extract_data_from_page_source(r.text)
            results.append(data)
        if self.dump_folder:
            json.dump(results,open(self.dump_folder+str(zone_id)+'__'+timestamp()+'.json','a'))
        return results
    
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

    def extract_data_from_page_source(self,html_body, formatting='JSON',enable_val_skip=True,enable_simple=True):
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
#            return None
        start_ix=start_ix+len(trigger)-1
        if enable_simple:
            end_ix=html_body.find('</script>',start_ix)
        else:
        
            c_d={'{':1,'}':-1}
            skip_val='"'
            balance=0
            ix=start_ix
            balance_achieved=False
            while not balance_achieved:
                char=html_body[ix]
                if char == "{" or char =="}":
                    balance=balance+c_d[char]
                if char==skip_val and enable_val_skip:
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
            print('Please choose formatting as JSON')
            return locals()#html_body[start_ix:end_ix]
    def store_failures(self):
        fail_dic_list=[]
        for i in self.failed_list:
            fail_dic={}
            fail_dic['fun']=i['Source']
            fail_dic['url']=i['response'].url
            fail_dic['html']=i['response'].text
            fail_dic['status_code']=i['response'].status_code
            fail_dic_list.append(fail_dic)
        if fail_dic_list:
            json.dump(fail_dic_list,open('failed_list.json','a'))
        
def write_response_text(r,path):
    f = open(path,'a')
    f.write(r.text)
    f.close()
    return 0    
if __name__=='__main__': 
    handler=rightmove_handler()
#    r=handler.get_all_houses_for_rent()
#    r=handler.get_all_houses_for_sale()
#    handler.store_failures()
    sales_folder='outcome_2020_04_19_20_50_24_sale'
    rent_folder='outcome_2020_04_19_22_29_41_rent'