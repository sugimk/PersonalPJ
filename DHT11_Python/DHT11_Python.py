import RPi.GPIO as GPIO
import dht11
import time
import datetime

## Define GPIO to LCD mapping
Temp_sensor=14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers initialize GPIO

# read data using pin 14
instance = dht11.DHT11(pin = Temp_sensor)

try:
    while True:
        #get DHT11 sensor value
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            
            time.sleep(6) # 6 second delay

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
