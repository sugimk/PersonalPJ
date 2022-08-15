import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

try:
	while True:
	    result = instance.read()
	    #if result.is_valid():
        #od = "Temperature: %-3.1f C" % result.temperature
        #hm = "%-3.1f %%" % result.humidity
	    print("Last valid input: " + str(datetime.datetime.now()))
	    print("Temperature: %-3.1f C" % result.temperature)
        #print(od)
	    print("Humidity: %-3.1f %%" % result.humidity)
        #print("Humidity: %d %%" % hm)
        #Client.publish(Topic, )
	    time.sleep(3)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()