# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from random import choice, shuffle
from requests_html import HTMLSession
#session = HTMLSession()
test_url='https://httpbin.org/ip'
url='https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=OUTCODE%5E2509&insId=2&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'


#r = session.get(url)
def get_proxy():
    url="https://www.sslproxies.org/"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    a=list(zip(map(lambda x:x.text,soup.findAll('td')[::8]),
    map(lambda x:x.text,soup.findAll('td')[1::8])))
    x=list(map( lambda x:x[0]+':'+x[1], a))
    return {'https':choice(x)}
#%%
def get_proxy_list(out_format='str'):
    url="https://www.sslproxies.org/"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    a=list(zip(map(lambda x:x.text,soup.findAll('td')[::8]),
    map(lambda x:x.text,soup.findAll('td')[1::8])))
    a=[(x[0],x[1]) for x in a if x[1].isnumeric()]
    if out_format=='tuple':
        return a
    elif out_format=='str':
        x=list(map( lambda x:x[0]+':'+x[1], a))
        return x
#%%
def proxy_request(request_type,url,**kwargs):
    while True:
        proxy=get_proxy()
       
        try: 
            print("Using proxy: {}".format(proxy))
#r = session.get(url)
            session = HTMLSession(browser_args=["--proxy-server=x.x.x.x:xxxx"])
            r=  session.request(request_type,url,proxies=proxy,timeout=5,**kwargs)
            
#            r= requests.request(request_type,url,proxies=proxy,timeout=5,**kwargs)
            break
        except:
            print("Failed to use proxy: {}".format(proxy))
            pass
    return r

def give_me_a_succesfull_HTMLSession(test_url='https://httpbin.org/ip'):
#    sample_page_source='{\n\n  "origin": "95.146.110.236" \n\n}'
    proxy_list=get_proxy_list()
    shuffle(proxy_list)
#    proxy_address=choice(proxy_list)
    for proxy_address in proxy_list:
        print("Trying: "+proxy_address)
        try:
            session = HTMLSession()
            session.proxies.update({'http': 'http://'+proxy_address,'https': 'https://'+proxy_address})
            r=  session.request('get',test_url,timeout=5)
            r=  session.request('get',test_url,timeout=5)
            if r.status_code==200:
                html=r.text
            if len(html)<220:
               return session
            else:
                del session
        except:
            if 'session' in locals():
                del session
            pass
    print("Sorry no IPs left to try with!")
    return None

session=give_me_a_succesfull_HTMLSession()
r=  session.request('get',url,timeout=5)
f=open('outcome.html','a')
f.write(r.text)
f.close()
