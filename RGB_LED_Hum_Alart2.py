import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sys                          #sysモジュールをインポート

## Define GPIO to LCD mapping
Temp_sensor=14

Led_red_pin = 25                         #変数"Led_red_pin"に25を格納
Led_green_pin = 17                      #変数"Led_green_pin"に17を格納
Led_blue_pin = 18                       #変数"Led_blue_pin"に18を格納

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers initialize GPIO
GPIO.setup(Led_red_pin, GPIO.OUT)        #GPIO25を出力モードに設定
GPIO.setup(Led_green_pin, GPIO.OUT)     #GPIO23を出力モードに設定
GPIO.setup(Led_blue_pin, GPIO.OUT)      #GPIO18を出力モードに設定

# read data using pin 14
instance = dht11.DHT11(pin = Temp_sensor)
              
try:
   while True:
#get DHT11 sensor value
        result = instance.read()
        if result.is_valid():
            humi = round(result.humidity)
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % humi)
            #print("Humidity: %d %%" % result.humidity)
            
            humi = int(humi)
            print (humi)

            if humi >= 80:
                GPIO.output(Led_red_pin, GPIO.HIGH)    #GPIO22 High(3.3V) 「赤点灯」
                time.sleep(1)                          #1秒間待つ
                GPIO.output(Led_red_pin, GPIO.LOW)     #GPIO22 Low(0V) 「赤消灯」
                time.sleep(1)                          #1秒間待つ
            elif 60 <= humi < 80:
                GPIO.output(Led_green_pin, GPIO.HIGH)   #GPIO23 High(3.3V) 「青点灯」
                time.sleep(2)                           #2秒間待つ
                GPIO.output(Led_green_pin, GPIO.LOW)    #GPIO23 Low(0V) 「青消灯」
                time.sleep(2)                           #2秒間待つ
            else:
                GPIO.output(Led_blue_pin, GPIO.HIGH)    #GPIO12 High(3.3V) 「緑点灯」
                time.sleep(3)                           #3秒間待つ
                GPIO.output(Led_blue_pin, GPIO.LOW)     #GPIO12 Low(0V) 「緑消灯」
                time.sleep(3)                           #3秒間待つ

            #time.sleep(3) # 3 second delay

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
    sys.exit()
