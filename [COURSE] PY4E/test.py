# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
# The program will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data,compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL:')
if len(url) < 1:
    url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_501607.xml').read()
else:
    url = urllib.request.urlopen('url').read()

count = 0
tree = ET.fromstring(url) #Make trees of the string entered (url)
comments = tree.findall('.//comment') #Acces the comment tree from the root tag(.//<tag>) and puts them all in a list
for each in comments:
    comment_counts = (each.find('count').text) #Find the <count> tag and extracts the text in it
    count += int(comment_counts)
print(count)


# ## CLEANER ALTERNATIVE ##
#
# total_count = 0
# tree = ET.fromstring(url)
# counts = tree.findall('comments/comment/count') #Access directly from the root tag to the count tag
# for each in counts:
#     total_count += int(each.text) #Subtract the text of the tag, make it integer and sum to the total_count
# print(total_count)
