#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse 
import json 
import time

api_url = "http://api.carriots.com/streams"
device  = "RasPi-Home@JaimeDeArcos.JaimeDeArcos" # Replace with the ~id_developer" of your device
api_key = "9da965f1556c599c0696f210115e88fcc1367859b7817ac3b83d8fda84364816"	# Replace with your apikey
 
# Get the time
timestamp = int(time.time())

# Parameters - Body (data) 
params = {"protocol": "v2",
		  "device": device ,
		  "at": timestamp ,
		  "data": dict(temp=20, hum=50)}

binary_data = json.dunps(params).encode('ascii')
 

#Header 
header = {"User-Agent": "raspberrycarriots",
		  "Content-Type": "application/json",
		  "carriots.apikey": api_key}

# Request
req = urllib.request.Request(api_url,binary_data,header)
f = urllib.request.urlopen(req)

# Prit results
data = json.loads(f.read().decode('utf-8'))

#Print response 
#print(f.read().decode('utf-8'))

#Print in a pretty way
print(json.dumps(data,indent=4,sort_keys=True))

