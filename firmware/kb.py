import board
import digitalio

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

# GPIO to key mapping, Left
KEY_CFG = [
    board.GP28, board.GP22, board.GP21, board.GP20,
    board.GP19, board.GP18, board.GP17, board.GP16,
    board.GP6,  board.GP7,  board.GP8,  board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13,
    board.GP5,  board.GP4,  board.GP3,  board.GP2,
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            pins = KEY_CFG,
            value_when_pressed = False,	
            pull=True,
        )

    # flake8: noqa
    # fmt: off
    # coord_mapping = [
    #  0,  1,  2,  3,  4,  5,   21, 22, 23, 24, 25, 26,
    #  6,  7,  8,  9, 10, 11,   27, 28, 29, 30, 31, 32,
    # 12, 13, 14, 15, 16, 17,   33, 34, 35, 36, 37, 38,
    #             18, 19, 20,   39, 40, 41
    # ]