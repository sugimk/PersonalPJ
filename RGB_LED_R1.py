# 必要なモジュールをインポート
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import time                         #時間制御用のモジュールをインポート

#ポート番号の定義
Led_red_pin = 25                         #変数"Led_red_pin"に25を格納
Led_Blue_pin = 17                      #変数"Led_yellow_pin"に23を格納
Led_green_pin = 18                       #変数"Led_green_pin"に18を格納

#GPIOの設定
GPIO.setmode(GPIO.BCM)                   #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Led_red_pin, GPIO.OUT)        #GPIO25を出力モードに設定
GPIO.setup(Led_Blue_pin, GPIO.OUT)     #GPIO23を出力モードに設定
GPIO.setup(Led_green_pin, GPIO.OUT)      #GPIO18を出力モードに設定

#for文で5回繰り返す
for i in range(5):
    GPIO.output(Led_red_pin, GPIO.HIGH)     #GPIO25の出力をHigh(3.3V)にする
    time.sleep(0.5)                         #0.5秒間待つ
    GPIO.output(Led_red_pin, GPIO.LOW)      #GPIO25の出力をLow(0V)にする
    GPIO.output(Led_Blue_pin, GPIO.HIGH)  #GPIO23の出力をHigh(3.3V)にする
    time.sleep(0.5)                         #0.5秒間待つ
    GPIO.output(Led_Blue_pin, GPIO.LOW)   #GPIO23の出力をLow(0V)にする
    GPIO.output(Led_green_pin, GPIO.HIGH)   #GPIO18の出力をHigh(3.3V)にする
    time.sleep(0.5)                         #0.5秒間待つ
    GPIO.output(Led_green_pin, GPIO.LOW)    #GPIO18の出力をLow(0V)にする

GPIO.cleanup()                      #GPIOをクリーンアップ