print("starting")

import board
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

from kmk.extensions.RGB import RGB
from kmk.extensions.buzzer import Buzzer

from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

from kmk.handlers.sequences import send_string


keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

#encoders
encoder_map = [
    [
        (KC.VOLD,KC.VOLU,1),
        (KC.BRGD,KC.BRGI,1),
    ],
]
#encoder
encoder_ext = EncoderHandler([board.GP26, board.GP16],[board.GP27, board.GP17], encoder_map)
keyboard.modules.append(encoder_ext)
#RGB
'''
rgb_ext = RGB(pixel_pin=board.GP14, num_pixels=2)
keyboard.extensions.append(rgb_ext)
'''
#buzzer test 
buzz = Buzzer()
keyboard.extensions.append(buzz)

keyboard.col_pins = (board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP21,board.GP20,board.GP19,board.GP18,board.GP22)
keyboard.row_pins = (board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
	#QWERTY
	[																										   #ROTARY ENCODERS
		KC.ESC,  KC.Q,    KC.W,  KC.E,   KC.R,  KC.T,   KC.Y,   KC.U,    KC.I,     KC.O,    KC.P,    KC.BSPC,  KC.MPLY,
		KC.TAB,  KC.A,    KC.S,  KC.D,   KC.F,  KC.G,   KC.H,   KC.J,    KC.K,     KC.L,    KC.GRV,  KC.LSFT(KC.BSLS),  KC.MUTE,
		KC.LSFT, KC.Z,    KC.X,  KC.C,   KC.V,  KC.B,   KC.N,   KC.M,    KC.COMMA, KC.DOT,  KC.UP,   KC.ENT,   XXXXXXX,
		KC.LCTL, KC.LALT, KC.MO(1),   KC.SPC, KC.MO(2), KC.SPC, KC.SPC, KC.RALT, KC.NO,    KC.LEFT, KC.DOWN, KC.RIGHT, XXXXXXX,
	],
	#NUMBERS
	[																										   	   #ROTARY ENCODERS
		KC.TO(3), _______, _______, _______, _______, _______, KC.PAST, KC.P7,   KC.P8,  KC.P9,   KC.PSLS, _______, KC.MPLY,
		_______, _______, _______, _______, _______, _______, KC.PPLS, KC.P4,   KC.P5,  KC.P6,   KC.PMNS, _______, KC.MUTE,
		_______, _______, _______, _______, _______, _______, _______, KC.P1,   KC.P2,  KC.P3,   KC.PGUP, KC.MINS, _______,
		_______, _______, _______, _______, _______, _______, _______, _______, KC.P0,  KC.HOME, KC.PGDN, KC.END,  _______,
	],
	#LOWER
	[																										   	   #ROTARY ENCODERS
		_______, KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.LBRC, _______, KC.MNXT,
		_______, _______, _______, _______, _______, _______, _______, KC.LSFT(KC.RBRC), KC.LSFT(KC.RBRC), KC.RBRC, KC.SCLN, KC.LSFT(KC.QUOT), KC.MPRV,
		_______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.SLASH, _______,
		_______, _______, _______, _______, _______, _______, _______, _______, _______, KC.MPRV, KC.MPLY, KC.MNXT, _______,
	],
	#MUSIC
	[
		KC.DF(0), KC.NOTE_C5, KC.NOTE_CS5, KC.NOTE_D5, KC.NOTE_DS5, KC.NOTE_E5, KC.NOTE_F5, KC.NOTE_FS5, KC.NOTE_G5, KC.NOTE_GS5, KC.NOTE_A5, KC.NOTE_AS5, _______,
		KC.NOTE_B3,  KC.NOTE_C4, KC.NOTE_CS4, KC.NOTE_D4, KC.NOTE_DS4, KC.NOTE_E4, KC.NOTE_F4, KC.NOTE_FS4, KC.NOTE_G4, KC.NOTE_GS4, KC.NOTE_A4, KC.NOTE_AS4, _______,
		_______,  KC.NOTE_C3, KC.NOTE_CS3, KC.NOTE_D3, KC.NOTE_DS3, KC.NOTE_E3, KC.NOTE_F3, KC.NOTE_FS3, KC.NOTE_G3, KC.NOTE_GS3, KC.NOTE_A3, KC.NOTE_AS3, _______,
		KC.MELODY, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
	],
]

if __name__ == '__main__':
	led = digitalio.DigitalInOut(board.LED)
	led.direction = digitalio.Direction.OUTPUT
	led.value = True
	buzz.play_melody(name="startup")
	keyboard.go()