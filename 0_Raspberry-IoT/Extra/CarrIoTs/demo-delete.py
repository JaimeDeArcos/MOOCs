
''' 
Este script borra un stream de carriots 
(identificado por el apiurl)
'''

#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json

#OJO Con la url la barra al final
api_url ="http://api.carriots.com/streams/74370fc59294594be1f17491b814a807e9ae4ebd3c29a05097726bf2af0d9e0f@JaimeDeArcos.JaimeDeArcos/"       
api_key = "9da965f1556c599c0696f210115e88fcc1367859b7817ac3b83d8fda84364816" # Replace with your ApiKey 

#Parameters - Body  
params = { }  
binary_data = json.dumps(params).encode('ascii')

#Header 
header = {"carriots.apikey": api_key}

#Request 
req = urllib.request.Request(api_url,binary_data,header)
req.get_method = lambda:"DELETE"
f = urllib.request.urlopen(req)

#Print response 
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))