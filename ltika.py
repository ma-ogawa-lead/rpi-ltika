# import
import time
import RPi.GPIO as GPIO

# GPIOピン番号で利用する設定
GPIO.setmode(GPIO.BCM)

# 利用するGPIOピン設定
pin = 26
GPIO.setup(pin, GPIO.OUT)

# 無限ループ
while True:
    # 設定したGPIOピンにデータ送信(LED ON)
    GPIO.output(pin, 1)

    # 待機
    time.sleep(0.1)

    # 設定したGPIOピンにデータ送信(LED OFF)
    GPIO.output(pin, 0)

    # 待機
    time.sleep(0.1)
