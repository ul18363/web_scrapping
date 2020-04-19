import requests
from bs4 import BeautifulSoup
from random import choice

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
            r= requests.request(request_type,url,proxies=proxy,timeout=5,**kwargs)
            break
        except:
            print("Failed to use proxy: {}".format(proxy))
            pass
    return r


    
    
#url="https://www.sslproxies.org/"
#r=requests.get(url)
#soup=BeautifulSoup(r.content,'html5lib')
#
#
#a=list(zip(map(lambda x:x.text,soup.findAll('td')[::8]),
#map(lambda x:x.text,soup.findAll('td')[1::8])))
#x=list(map( lambda x:x[0]+':'+x[1], a))
url="https://youtube.com"
r=proxy_request('get',url)
#%%
################################
# ---  WebDriver with Proxy  ---
################################
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
#%%
#proxy_list=get_proxy_list()
#proxy_address=choice(proxy_list)
proxy_list=get_proxy_list()
proxy_address=choice(proxy_list)
##%% Try 1
#
#prox = Proxy()
#prox.proxy_type = ProxyType.MANUAL
#prox.http_proxy = proxy_address
##prox.socks_proxy = proxy_address
#prox.socks_proxy = proxy_address
#prox.socksVersion=5
#prox.ssl_proxy = proxy_address
##"socksVersion": 4
#capabilities = webdriver.DesiredCapabilities.CHROME
##capabilities['proxy']['socksProxy']=int(capabilities['proxy']['socksProxy'])
#prox.add_to_capabilities(capabilities)
#
#driver = webdriver.Chrome(desired_capabilities=capabilities)
##%% Try 2
#options = webdriver.ChromeOptions()
#proxy = Proxy()
#proxy.proxyType = ProxyType.MANUAL
#proxy.autodetect = False
#proxy.httpProxy = proxy.sslProxy = proxy.socksProxy = proxy_address
#options.Proxy = proxy
#options.add_argument("ignore-certificate-errors")
#driver = webdriver.Chrome(chrome_options=options) 

#%% Try 3 -> This works!
abs_path='/media/bruno/Extra/Ubuntu-Repository/personal_repo/web_scrapping/experimental_features/proxy_rerouting/'
proxy_address='201.64.22.50:8081'
driver_path=abs_path+'chromedriver'
manifest_path=abs_path+'manifest.json'
profile_path='Default'
#profile_path=abs_path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy_address)
#chrome_options.add_argument('--proxy-server="socks5://{}"'.format(proxy_address))
chrome_options.add_argument('--user-data-dir="{}"'.format(manifest_path))
chrome_options.add_argument('--profile-directory='+profile_path)

#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(driver_path,chrome_options=chrome_options) 

url="https://httpbin.org/ip"
driver.get(url)
#%%
driver.close()
del driver
#%%

#driver = webdriver.Chrome(desired_capabilities=capabilities)
###
## '--proxy-server="socks5://{}"'.format(proxy_address)
#dr