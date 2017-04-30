#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import Json
import time

api_url = "http:api.carriots.com/streas"
device = ".."  # Replace with the 'id_developer' of your device
api_key = "9da965f1556c599c0696f210115e88fcc1367859b7817ac3b83d8fda84364816" # Replace with your ApiKey 

# Sensor should be set to Adafruit_DHT.DHT11
sensor =Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# conected to GPIO23

# Try to get sensor reading. Use the read_retry method which will retry
# up to 15 times to get a sensor reading
# (waiting 2 sec beetween each retry).
humidity, temperature= Adafruit_DHT.read_retry(sensor,pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor)
# if this happens try again
if humidity is not None and temperature is not None:
	print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature,humidity))
	timestamp = int(time.time())
	params = {"protocol":"v2",
			  "device":device,
			  "at":timestamp,
			  "data": dict(temp=temperature,hum=humidity)}
	binary_data = json.dumps(params).encoder('ascii')
	header = {"User-Agent": "raspberrycarriots",
			  "Content-Type": "application/json",
			  "carriots.apikey": api_key}
	req = urllib.request.Request(api_url,binary_data,header)
	f = urllib.request.urlopen(req)
	print(f.read().decode('utf-8'))

else:
	print('Failed to get reading. Try again!')

