# Following Links in Python
# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = 1
#Repeat 7 times the loop
for each in range(0,7):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag_pos = tags[17]
    url = tag_pos.get('href', None)
    print(url)
    print(count, 'times looped')
    count += 1
