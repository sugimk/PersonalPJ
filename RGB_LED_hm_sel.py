# 必要なモジュールをインポート
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import time                         #時間制御用のモジュールをインポート
import sys                          #sysモジュールをインポート

#ポート番号の定義
Led_red_pin = 25                         #変数"Led_red_pin"に25を格納
Led_green_pin = 17                      #変数"Led_green_pin"に17を格納
Led_blue_pin = 18                       #変数"Led_blue_pin"に18を格納

#GPIOの設定
GPIO.setmode(GPIO.BCM)                   #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Led_red_pin, GPIO.OUT)        #GPIO25を出力モードに設定
GPIO.setup(Led_green_pin, GPIO.OUT)     #GPIO23を出力モードに設定
GPIO.setup(Led_blue_pin, GPIO.OUT)      #GPIO18を出力モードに設定

#湿度の入力
humi = int(input("湿度を入力："))
# humi = 100
print (humi)

#while文で無限ループ
#GPIOの電圧を制御
while True:
   
    try:

        if humi >= 90:
            GPIO.output(Led_red_pin, GPIO.HIGH)    #GPIO22 High(3.3V) 「赤点灯」
            time.sleep(1)                          #1秒間待つ
            GPIO.output(Led_red_pin, GPIO.LOW)     #GPIO22 Low(0V) 「赤消灯」
            time.sleep(1)                          #1秒間待つ
        elif 80 <= humi < 90:
            GPIO.output(Led_green_pin, GPIO.HIGH)   #GPIO23 High(3.3V) 「青点灯」
            time.sleep(2)                           #2秒間待つ
            GPIO.output(Led_green_pin, GPIO.LOW)    #GPIO23 Low(0V) 「青消灯」
            time.sleep(2)                           #2秒間待つ
        else:
            GPIO.output(Led_blue_pin, GPIO.HIGH)    #GPIO12 High(3.3V) 「緑点灯」
            time.sleep(3)                           #3秒間待つ
            GPIO.output(Led_blue_pin, GPIO.LOW)     #GPIO12 Low(0V) 「緑消灯」
            time.sleep(3)                           #3秒間待つ
    except KeyboardInterrupt:                  #Ctrl+Cキーが押された
        GPIO.cleanup()                         #GPIOをクリーンアップ
        sys.exit()                             #プログラムを終了