# Extracting Data from JSON
#
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below.

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#URL input
url = input('Enter URL:')

#Retrieve the URL, read and decode it
print('Retrieving', url)
open_url = urllib.request.urlopen(url, context=ctx)
data = open_url.read().decode()
#check
print('Retrieved', len(data), 'characters')
print('This URL contains:', data)

#Loads the data as a JSON file
json_file = json.loads(data)

#Extract the data I want from the JSON file and sum it
count = 0
for each in json_file['comments']:
    count += each['count']
print('Total count:', count)
