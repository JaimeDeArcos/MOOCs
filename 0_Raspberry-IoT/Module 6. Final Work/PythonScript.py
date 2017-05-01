'''
Final Work for MOOC
Practical Internet of Things (loT) with RaspberryPi
Author: Jaime de Arcos Sánchez

This script conects to 2 sensors:
	- DHT11 : Humidity & Temperature
	- BMP085: Barometric (altitude)
and sends to carriots
'''  

#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import Json
import time
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT

"http://api.carriots.com/devices/RasPi-Home@JaimeDeArcos.JaimeDeArcos/streams/?order=-1"

api_url = "http://api.carriots.com/streams"
device  = "RasPi-Home@JaimeDeArcos.JaimeDeArcos" # Replace with the ~id_developer" of your device
api_key = "9da965f1556c599c0696f210115e88fcc1367859b7817ac3b83d8fda84364816"	# Replace with your apikey
 
# Sensor 1 -> Adafruit DHT11
sensor_1 = Adafruit_DHT.DHT11
# Sensor 2 -> BMP085
sensor_2 = BMP085.BMP085()


# Try to read values from sensor.
# The read_retry function tries 15 times.
humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

# Read the BMP085
altitude = sensor_2.read_sealevel_pressure())


if humidity is not None and temperature is not None and altitude is not None:

	# log the data to the console
	print('Temp={0:0.1f}*C Humidity={1:0.1f}% altitude={0:0.2f}%'.format(temperature,humidity,altitude))
	
    #Data
    data = dict(temp=temperature,hum=humidity,alt=altitude)

    #Actual time
	timestamp = int(time.time())

	# Set the params and do the request
	params = {"protocol":"v2",
			  "device": device,
			  "at":timestamp,
			  "data": data}
	binary_data = json.dumps(params).encoder('ascii')
	header = {"User-Agent": "raspberrycarriots",
			  "Content-Type": "application/json",
			  "carriots.apikey": api_key}
	req = urllib.request.Request(api_url,binary_data,header)
	f = urllib.request.urlopen(req)

	# Print the response
	print(f.read().decode('utf-8'))

else:
	# If something goes wrong, log in the console  
	print('Failed to get reading. Try again!')

