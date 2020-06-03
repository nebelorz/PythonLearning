# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter URL:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup) #check

# Retrieve all span tags
count = 0
tags = soup('span')
for tag in tags:
    tag = str(tag)
    find_numbers = re.findall('[0-9]+', tag) #find any number in each line of the file, greedy-wise. (and puts it/them in a list)
    for each in find_numbers:
        count = count + int(each)
print(count)
