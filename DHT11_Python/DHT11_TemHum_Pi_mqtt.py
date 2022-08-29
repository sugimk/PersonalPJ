from telnetlib import TM
from tempfile import tempdir
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import paho.mqtt.client as mqtt

###### Edit variables to your environment #######
broker_address = "test.mosquitto.org"     #MQTT broker_address :192.168.0.31
Topic = "sugi3pitest"

## Define GPIO to LCD mapping
Temp_sensor=14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers initialize GPIO

# read data using pin 14
instance = dht11.DHT11(pin = Temp_sensor)

print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

try:
    while True:
        #get DHT11 sensor value
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
            #client.publish(Topic, result.temperature)
            client.publish(Topic, result.humidity)
            time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
    print ("GPIO cleeanup and end!")