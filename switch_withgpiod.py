# import
import gpiod
import time
import os
from datetime import timedelta

# チップセット設定
chip = gpiod.chip(0)
# 利用するGPIOピン番号設定
pin = 21
# ボタンモード設定
BUTTON_EDGE = gpiod.line_request.EVENT_BOTH_EDGES
# チップセットとGPIOピンの紐づけ
button = chip.get_line(pin)

# 利用種別設定
config = gpiod.line_request()
config.consumer = "Button"
config.request_type = BUTTON_EDGE
button.request(config)

# 無限ループ
while True:
    # 指定秒数居ないの処理か確認
    if button.event_wait(timedelta(seconds=10)):
        event = button.event_read()
        # ボタンイベント種別確認
        if event.event_type == gpiod.line_event.RISING_EDGE:
            # 出力
            print("スイッチON")
        else:
            # 出力
            print("スイッチOFF")
    else:
            # 出力
        print("タイムアウト")
