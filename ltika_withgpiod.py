# import
import gpiod

# チップセット設定
chip = gpiod.chip(0)
# 利用するGPIOピン番号設定
pin = 26
# チップセットとGPIOピンの紐づけ
gpiod_pin = chip.get_line(pin)

# 利用種別設定
config = gpiod.line_request()
config.consumer = "Blink"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

# GPIOピンへ利用種別紐づけ
gpiod_pin.request(config)

# LEDチカ
gpiod_pin.set_value(1)
