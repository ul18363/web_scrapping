import requests
from bs4 import BeautifulSoup
from random import choice,shuffle
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

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


def give_me_a_succesfull_driver():
#    sample_page_source='{\n\n  "origin": "95.146.110.236" \n\n}'
    proxy_list=get_proxy_list()
    shuffle(proxy_list)
#    proxy_address=choice(proxy_list)
    abs_path='/media/bruno/Extra/Ubuntu-Repository/personal_repo/web_scrapping/experimental_features/selenium_with_proxy/'
    for proxy_address in proxy_list:
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
        if len(driver.page_source)<100:
           return driver
        else:
            driver.close()
            del driver #Is not enough to close it!
            
    print("Sorry no IPs left to try with!")
    return None





#display = Display(visible=0, size=(800, 600))
#display.start()

# Do Not use headless chrome option
# options.add_argument('headless')
#%%
# First solution using  pyvirtualdisplay and xvfb(as dependency)
#from pyvirtualdisplay import Display

#url = 'https://10.11.227.21/tmui/'
#driver.get(url + "login.jsp")
#
#html_source = driver.page_source
#print(html_source)
#
#blocStatus = WebDriverWait(driver,    TIMEOUT).until(EC.presence_of_element_located((By.ID, "username")))
#inputElement = driver.find_element_by_id("username")
#inputElement.send_keys('actualLogin')
#inputElement = driver.find_element_by_id("passwd")
#inputElement.send_keys('actualPassword')
#inputElement.submit()
#
#display.stop()
#



from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

#%%
driver=None    
#driver=give_me_a_succesfull_driver()
#%%  
proxy_list=get_proxy_list()
i=-1
#%%
#shuffle(proxy_list)
i=i+1
if i>0:
    driver.close()
    del driver
#    proxy_address=choice(proxy_list)
abs_path='/media/bruno/Extra/Ubuntu-Repository/personal_repo/web_scrapping/experimental_features/selenium_with_proxy/'
#for proxy_address in proxy_list:
#i=0
proxy_address=proxy_list[i]
print("Trying: ["+proxy_address+"]")
#proxy_address='201.64.22.50:8081'
driver_path=abs_path+'chromedriver'
manifest_path=abs_path+'manifest.json'
profile_path='Default'
#profile_path=abs_path
#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--proxy-server=http://'+proxy_address)
#chrome_options.add_argument('--proxy-server="socks5://{}"'.format(proxy_address))
chrome_options.add_argument('--user-data-dir="{}"'.format(manifest_path))
chrome_options.add_argument('--profile-directory='+profile_path)
#chrome_options.add_argument('--headless') # We lose HTML pagesource when going headless! #For chrome at least
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(chrome_options = chrome_options,executable_path=driver_path,desired_capabilities=capabilities)

#driver = webdriver.Chrome(driver_path,chrome_options=chrome_options) 

url="https://httpbin.org/ip"
driver.get(url)
print(driver.page_source)