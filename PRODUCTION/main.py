import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Khai báo các chân GPIO tương ứng theo mạch KiCad
keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4, board.D5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Sơ đồ 9 phím Numpad (từ 1 đến 9)
keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
    ]
]

if __name__ == '__main__':
    keyboard.go()