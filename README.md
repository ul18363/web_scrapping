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

