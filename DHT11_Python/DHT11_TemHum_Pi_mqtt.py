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

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

print("creating new instance")
client = mqtt.Client("pub5") #create new instance

print("connecting to broker")
client.connect(broker_address) #connect to broker

try:
    while True:
        result = instance.read()
        #if result.is_valid():

        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        #client.publish(Topic, result.temperature)
        client.publish(Topic, result.humidity)
        time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
    print ("GPIO cleeanup and end!")