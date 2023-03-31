import time
import board
import adafruit_dht
import psutil
import serial
import http.client
import urllib

key = "O4V9M6O4LMOJNXKH"

def send_data():
        
    temp = sensor.temperature
    humidity = sensor.humidity
    print("Temperature: {} *C Humidity: {} %".format(temp,humidity))
    params = urllib.parse.urlencode({'field1': temp,'field2':humidity,'key':key})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except:
        print("connection failed")

sensor = adafruit_dht.DHT11(board.D23)
while True:

    
    send_data()
    
    time.sleep(5)
    