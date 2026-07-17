#Lily-Pad

import time
import board
import busio
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros
from kmk.modules import Module

#keyboard

keyboard = KMKKeyboard()

#matrix 

keyboard.col_pins = (board.GP1, board.GP2, board.GP3)

keyboard.row_pins = (board.GP4, board.GP7)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

#encoder

encoder_handler = EncoderHandler

keyboard.modules.append(encoder_handler)

encoder_handler.pins = (board.GP10, board.GP11)

#layers

layers = Layers()

keyboard.modules.append(layers)

#macros

macros = Macros()
keyboard.modules.append(macros)

MSG_MACRO = KC.MACRO("Sent from my Lily-Pad", KC.ENTER)

#keymap CTRL C , MUTE, CTRL V, CTRL Z, CTRL S, SWITCH TO LAYER 1

keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.MUTE, KC.LCTL(KC.V), KC.LCTL(KC.Z),
        KC.LCTL(KC.S),KC.MO(1)
    ],

    [
        KC.MPLY, KC.TRNS, KC.MNXT,
        MSG_MACRO, KC.MPREV, KC.TRNS
    ]
]

#encoder thingys

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
    ((KC.BRIU, KC.BRID),),
]

#OLED DISPLAY

#IT SHOWS THE TITLE, CURRENT LAYER and LAST KEY PRESSED (title_label, layer_label and key_label do this)

import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

displayio.release_displays()

OLED_width = 128
OLED_height = 32
OLED_addr = 0x3C

i2c = busio.I2C(scl=board.GP6, sda = board.GP5)

display_bus = displayio.I2CDisplay(i2c, device_address= OLED_addr)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width = OLED_width, height = OLED_height)

splash = displayio.Group()
display.root_group = splash

title_label = label.Label(terminalio.FONT, text = 'Lily-Pad', x=2, y=4)
layer_label = label.Label(terminalio.FONT, text = 'Layer: Base', x=2, y=16)
key_label = label.Label(terminalio.FONT, text = 'Key: --', x=2, y= 27)

splash.append(title_label)
splash.append(layer_label)
splash.append(key_label)

LAYER_NAMES = {0: "Base", 1: "Macro"}



class OledStatus(Module):
    "Custom KMK module: keeps the OLED in sync with keyboard state"

    def __init__(self):
        self.last_update = 0 
        self.refresh_ms = 150


    def during_bootup(self,keyboard):
        return

    def before_matrix_scan(self,keyboard):
        return
    
    def after_matrix_scan(self,keyboard):
        return

    def process_key(self,keyboard,key, is_pressed, int_coord):
        if is_pressed:
            try:
                key_label.txt = "Key: {}".format(str(key.code))

            except AttributeError:
                key_label.txt = "Key: --" 

        return key
    
    def before_hid_send(self, keyboard):

        return
    
    def after_hid_send(self, keyboard):

        now = time.monotonic()*1000

        if now - self._last_update < self.refresh:
            return
        
        self._last_update = now
        active_layer = keyboard.active_layers[0] if keyboard.active_layers[0] else 0
        layer_label.text = "Layer: {}".format(LAYER_NAMES.get(active_layer, active_layer))

    def on_power_save_enable(self,keyboard):
        display.root_group = None

    def on_power_save_disable(self, keyboard):
        display.root_group = splash

keyboard.modules.append(OledStatus())


#LEDs

#I want LEDs to both flash when key pressed

leds = digitalio.DigitalInOut(board.GP9)

leds.direction = digitalio.Direction.OUTPUT

class ledIndicators (Module):
    def __init__(self):
        self.leds_off_at = 0 

    def during_bootup(self, keyboard):
        leds.value = False


    def before_matrix_scan(self, keyboard):
        return
    
    def after_matrix_scan(self, keyboard):
        return
    
    def process_key (self, keyboard, key, is_pressed, int_coord):
        if is_pressed:
            leds.value = True
            self.leds_off_at = time.monotonic * 1000 + 60
        return key
    
    def before_hid_send(self, keyboard):
        return
    
    def after_hid_send(self, keyboard):
        active_layer = keyboard.active_layers[0]if keyboard.active_layers else 0 


    def on_powersave_enable(self, keyboard):
        leds.value = False

    def on_powersave_disable(self, keyboard):
        return
    
keyboard.modules.append(ledIndicators())


if __name__ == "__main__":
    keyboard.go

    












            

    
    