# -*- coding: utf-8 -*-

"""
    https://free-proxy-list.net/
    https://sslproxies.org/
    
    IP Address	      Port	Code	Country	Anonymity	    Google	Https	Last Checked
    93.157.189.86	      50506	TR	Turkey	elite proxy	no	     yes  	1 minute ago
    195.123.212.199	  50302	LV	Latvia	elite proxy	no	     yes   	1 minute ago
"""
import requests
proxies={
        "https":"103.86.135.62:59538",
        "http":"103.86.135.62:59538"
        }

url="https://httpbin.org/ip"
r_local=requests.get(url)
print(r_local.json())
#%%
r_proxy=requests.get(url,proxies=proxies)
print(r_proxy.json())

