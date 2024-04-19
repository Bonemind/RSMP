import board
import digitalio

from kb import KMKKeyboard
from storage import getmount

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.tap_time = 100


layers = Layers()

# data_pin = board.GP1 if split_side == SplitSide.LEFT else board.GP0
# data_pin2 = board.GP0 if split_side == SplitSide.LEFT else board.GP1

layers_ext = Layers()
layers_ext.tap_time = 100

keyboard.modules = [layers_ext]
keyboard.extensions = []
#
# Cleaner key names
# _______ = KC.TRNS
# XXXXXXX = KC.NO

# LYR_LOWER = 1
# LYR_RAISE = 2
# LOWER = KC.MO(LYR_LOWER)
# RAISE = KC.MO(LYR_RAISE)
# ADJUST = KC.LT(3, KC.SPC)

# MT_RSEN = KC.MT(KC.ENT, KC.RSFT)
# KC_LRGR = KC.LT(LYR_LOWER, KC.GRV)
# KC_RSSP = KC.LT(LYR_RAISE, KC.SPC)

keyboard.keymap = [
    [  #QWERTY
        KC.A,    KC.B,    KC.C,    KC.D,
        KC.E,    KC.F,    KC.J,    KC.K,
        KC.L,    KC.M,    KC.N,    KC.O,
        KC.P,    KC.Q,    KC.R,    KC.S,
        KC.T,    KC.U,    KC.V,    KC.W,
    ],
]

if __name__ == '__main__':
    keyboard.go()