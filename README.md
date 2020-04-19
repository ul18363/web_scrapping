# web_scrapping
Note: The variable explorer from Spyder 4 is significantly slower to display variables and in some cases can't support many variables that previously could.
Thus is recommended to use Spyder 3 as the IDE. 

To make it functional:
- Install spyder3 : sudo apt-get install spyder3
- Make sure to use python3.6 (Is compatible with Python 3.6 [3.7+ didnt work for me]) 
- conda install ipykernel cloudpickle (on the environment you want to develop on)

 - Make sure that when calling python3.6 you are using the following one (in which spyder runs over)
    (base) bruno@bruno-Precision-3630-Tower:~$ which python3.6
    /usr/bin/python3.6
    
    sudo python3.6 -m pip install pandas
    sudo python3.6 -m pip install matplotlib
    sudo python3.6 -m pip install lxml

## Objective of Repository
To give an easy way to scrap sites from commercial assets and return parameters 
for further analysis

# Libraries used:
## BeautifulSoup4:
Beautiful Soup is a Python library for pulling data out of HTML and XML files.
 It works with your favorite parser to provide idiomatic ways of navigating, 
 searching, and modifying the parse tree. It commonly saves programmers hours
 or days of work.
 
### A little background on tags:
https://www.w3schools.com/tags/tag_a.asp
The <a> tag defines a hyperlink, which is used to link from one page to another.

The <form> element can contain one or more of the following form elements:

<input>
<textarea>
<button>
<select>
<option>
<optgroup>
<fieldset>
<label>
<output>

The <script> tag is used to define a client-side script (JavaScript).

## Selenium
Seleniums is 

# Sites:

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
    
Addiding index here also work (originally wasn't there)
    If index is greater than the number of results the value is ommited in the search (aka index is set to 0)
    If index is +-12 places from i*24 page i will appear

locationIdentifier: Amazingly the outer postcode area is represented by a number 1 or bigger.

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

