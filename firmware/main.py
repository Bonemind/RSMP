from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.tap_time = 100


layers = Layers()

layers_ext = Layers()
layers_ext.tap_time = 100

keyboard.modules = [layers_ext]
keyboard.extensions = []
#
# Cleaner key names
# _______ = KC.TRNS
# XXXXXXX = KC.NO

LAYER_ALT = 1
KCALT = KC.LT(LAYER_ALT, KC.SPC)

keyboard.keymap = [
    [  
        KC.A,    KC.B,    KC.C,    KC.D,
        KC.E,    KC.F,    KC.J,    KC.K,
        KC.L,    KC.M,    KC.N,    KC.O,
        KC.P,    KC.Q,    KC.R,    KC.S,
        KCALT,    KC.U,    KC.V,    KC.W,
    ],
    [  
        KC.N1,       KC.N2,       KC.N3,       KC.N4,
        KC.N5,       KC.N6,       KC.N7,       KC.N8,
        KC.N9,       KC.N0,       KC.LBRACKET, KC.RBRACKET,
        KC.QUOTE,    KC.COMMA,    KC.GRAVE,    KC.DOT,
        KC.SLASH,    KC.MINUS,    KC.EQUAL,    KC.ENTER,
    ],
]

if __name__ == '__main__':
    keyboard.go()