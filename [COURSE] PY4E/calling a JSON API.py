# Calling a JSON API
# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
# The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
# and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#API KEY, address and URL
api_key = 42
address = input('Enter address:')
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

#Making the request (address and key)
request = {'address': address, 'key': api_key}
final_url = serviceurl + urllib.parse.urlencode(request)
print(final_url) ## http://py4e-data.dr-chuck.net/json?address=&key=42

#Retrieve the URL, read and decode it
print('Retrieving', final_url)
open_url = urllib.request.urlopen(final_url, context=ctx)
data = open_url.read().decode()
#check
print('Retrieved', len(data), 'characters')
print('This URL contains:', data)

#Loads the data as a JSON file
json_file = json.loads(data)

#Extract the data I want from the JSON file
place_id = json_file['results'][0]['place_id'] #Get in the list 'results' and check the 'place_id value
print('Place ID:', place_id)
