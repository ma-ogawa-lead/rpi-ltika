# import
import time
import RPi.GPIO as GPIO

# GPIOピン番号で利用する設定
GPIO.setmode(GPIO.BCM)

# 利用するGPIOピン設定
pin = 21
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 無限ループ
while True:
    # 押されたことを検知するモードに設定
    GPIO.wait_for_edge(pin, GPIO.FALLING)

    # 出力
    print("スイッチON")

    # 待機(チャタリング対策)
    time.sleep(0.3)
