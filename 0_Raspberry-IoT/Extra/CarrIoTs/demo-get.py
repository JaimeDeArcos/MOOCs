#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import Json
import time

api_url = 'http://api.carriots.com/devices'
api_key = '9da965f1556c599c0696f210115e88fcc1367859b7817ac3b83d8fda84364816' # Replace with your ApiKey 

#Parameters - Body 
timestamp = int(time.time())
params = {"order": -1} # Reverse order. to get newest first 
binary_data = json.dums(params).encoder('ascii')

#Header 
header = {"User-Agent": "raspberrycarriots",
		  "Content-Type": "application/json",
		  "carriots.apikey": api_key}

#Request 
req = urllib.request.Request(api_url,binary_data,header)
f = urllib.request.urlopen(req)

#Print response 
print(f.read().decode('utf-8'))

#Print in a pretty way
#data=json.loads(f.read().decode('utf-8'))
#print(json.dumps(data,indent=4,sort_keys=True))

