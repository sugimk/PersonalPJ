import dht11
import RPi.GPIO as GPIO
import time
import datetime

# Define GPIO to LCD mapping
Temp_sensor=14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
instance = dht11.DHT11(pin = Temp_sensor)

try:
    while True:
        #get DHT11 sensor value
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

            time.sleep(3) # 3 second delay
        
except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()