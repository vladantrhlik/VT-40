from kmk.extensions import Extension
from kmk.keys import make_key
import board
import pulseio
from kmk.extensions.tones import tones
import time
from kmk.keys import KC

class Buzzer(Extension):
	def __init__(self):
		for n in tones.keys():
			make_key(names=(f'NOTE_{n}',), on_press= self.press, on_release=self.rel, data=n)

		make_key(names=(f'MELODY',), on_press= self.play, data="harry-potter")

		self.current_notes = []
		self.buzzer = pulseio.PWMOut(board.GP14, variable_frequency=True)

		#melody stuff
		self.mld_start = 0
		self.mld = []
		self.mld_playing = False
		self.mld_note = "OFF"
		self.mld_duration = 0

		self.melodies = {
			"startup": [["DS4", 100], ["FS4",100], ["FS5", 100]],
			"planck-sound": [["E7", 12], ["CS7", 8], ["E6", 8], ["A6", 8], ["CS7", 20]],
			"take-on-me": [['FS5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['D5', 125], ['OFF', 42], ['B4', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['B4', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['GS5', 125], ['OFF', 42], ['GS5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['B5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['D5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['D5', 125], ['OFF', 42], ['B4', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['B4', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['GS5', 125], ['OFF', 42], ['GS5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['B5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['D5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['D5', 125], ['OFF', 42], ['B4', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['B4', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['GS5', 125], ['OFF', 42], ['GS5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['B5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['A5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['D5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['OFF', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42], ['FS5', 125], ['OFF', 42], ['E5', 125], ['OFF', 42]],
			"zelda": [['D4', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['OFF', 139], ['OFF', 28], ['E4', 139], ['OFF', 28], ['B4', 556], ['OFF', 111], ['F4', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['OFF', 139], ['OFF', 28], ['E4', 139], ['OFF', 28], ['B4', 556], ['OFF', 111], ['D4', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['OFF', 139], ['OFF', 28], ['E4', 139], ['OFF', 28], ['B4', 556], ['OFF', 111], ['F4', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['OFF', 139], ['OFF', 28], ['E4', 139], ['OFF', 28], ['B4', 556], ['OFF', 111], ['D4', 139], ['OFF', 28], ['F4', 139], ['OFF', 28], ['D5', 556], ['OFF', 111], ['D4', 139], ['OFF', 28], ['F4', 139], ['OFF', 28], ['D5', 556], ['OFF', 111], ['E5', 278], ['OFF', 56], ['F5', 139], ['OFF', 28], ['E5', 139], ['OFF', 28], ['E5', 139], ['OFF', 28], ['E5', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['A4', 556], ['OFF', 111], ['A4', 278], ['OFF', 56], ['D4', 278], ['OFF', 56], ['F4', 139], ['OFF', 28], ['G4', 139], ['OFF', 28], ['A4', 556], ['OFF', 111], ['A4', 278], ['OFF', 56], ['D4', 278], ['OFF', 56], ['F4', 139], ['OFF', 28], ['G4', 139], ['OFF', 28], ['E4', 556], ['OFF', 111], ['D4', 139], ['OFF', 28], ['F4', 139], ['OFF', 28], ['D5', 556], ['OFF', 111], ['D4', 139], ['OFF', 28], ['F4', 139], ['OFF', 28], ['D5', 556], ['OFF', 111], ['E5', 278], ['OFF', 56], ['F5', 139], ['OFF', 28], ['E5', 139], ['OFF', 28], ['E5', 139], ['OFF', 28], ['E5', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['A4', 556], ['OFF', 111], ['A4', 278], ['OFF', 56], ['D4', 278], ['OFF', 56], ['F4', 139], ['OFF', 28], ['G4', 139], ['OFF', 28], ['A4', 556], ['OFF', 111], ['A4', 278], ['OFF', 56], ['D4', 1111], ['OFF', 222]],
			"doom": [['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['AS2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['B2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['AS2', 500], ['OFF', 167], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['AS2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['B2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['AS2', 500], ['OFF', 167], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['AS2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['B2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['AS2', 500], ['OFF', 167], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['AS2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['B2', 125], ['OFF', 42], ['C3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['D3', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['E2', 125], ['OFF', 42], ['FS3', 62], ['OFF', 21], ['D3', 62], ['OFF', 21], ['B2', 62], ['OFF', 21], ['A3', 62], ['OFF', 21], ['FS3', 62], ['OFF', 21], ['B2', 62], ['OFF', 21], ['D3', 62], ['OFF', 21], ['FS3', 62], ['OFF', 21], ['A3', 62], ['OFF', 21], ['FS3', 62], ['OFF', 21], ['D3', 62], ['OFF', 21], ['B2', 62], ['OFF', 21]],
			"tetris": [['E5', 278], ['OFF', 56], ['B4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['C5', 139], ['OFF', 28], ['B4', 139], ['OFF', 28], ['A4', 278], ['OFF', 56], ['A4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['E5', 278], ['OFF', 56], ['D5', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['B4', 278], ['OFF', 56], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['E5', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['A4', 139], ['OFF', 28], ['A4', 278], ['OFF', 56], ['B4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['F5', 139], ['OFF', 28], ['A5', 278], ['OFF', 56], ['G5', 139], ['OFF', 28], ['F5', 139], ['OFF', 28], ['E5', 278], ['OFF', 56], ['C5', 139], ['OFF', 28], ['E5', 278], ['OFF', 56], ['D5', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['B4', 278], ['OFF', 56], ['B4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['E5', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['OFF', 278], ['OFF', 56], ['E5', 278], ['OFF', 56], ['B4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['C5', 139], ['OFF', 28], ['B4', 139], ['OFF', 28], ['A4', 278], ['OFF', 56], ['A4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['E5', 278], ['OFF', 56], ['D5', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['B4', 278], ['OFF', 56], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['E5', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['A4', 139], ['OFF', 28], ['A4', 278], ['OFF', 56], ['B4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['F5', 139], ['OFF', 28], ['A5', 278], ['OFF', 56], ['G5', 139], ['OFF', 28], ['F5', 139], ['OFF', 28], ['E5', 278], ['OFF', 56], ['C5', 139], ['OFF', 28], ['E5', 278], ['OFF', 56], ['D5', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['B4', 278], ['OFF', 56], ['B4', 139], ['OFF', 28], ['C5', 139], ['OFF', 28], ['D5', 278], ['OFF', 56], ['E5', 278], ['OFF', 56], ['C5', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['A4', 278], ['OFF', 56], ['OFF', 278], ['OFF', 56], ['E5', 556], ['OFF', 111], ['C5', 556], ['OFF', 111], ['D5', 556], ['OFF', 111], ['B4', 556], ['OFF', 111], ['C5', 556], ['OFF', 111], ['A4', 556], ['OFF', 111], ['GS4', 556], ['OFF', 111], ['B4', 278], ['OFF', 56], ['OFF', 139], ['OFF', 28], ['E5', 556], ['OFF', 111], ['C5', 556], ['OFF', 111], ['D5', 556], ['OFF', 111], ['B4', 556], ['OFF', 111], ['C5', 278], ['OFF', 56], ['E5', 278], ['OFF', 56], ['A5', 556], ['OFF', 111], ['GS5', 556], ['OFF', 111]],
			"harry-potter": [['OFF', 694], ['OFF', 139], ['D4', 347], ['OFF', 69], ['G4', 347], ['OFF', 69], ['AS4', 174], ['OFF', 35], ['A4', 347], ['OFF', 69], ['G4', 694], ['OFF', 139], ['D5', 347], ['OFF', 69], ['C5', 694], ['OFF', 139], ['A4', 694], ['OFF', 139], ['G4', 347], ['OFF', 69], ['AS4', 174], ['OFF', 35], ['A4', 347], ['OFF', 69], ['F4', 694], ['OFF', 139], ['GS4', 347], ['OFF', 69], ['D4', 1389], ['OFF', 278], ['D4', 347], ['OFF', 69], ['G4', 347], ['OFF', 69], ['AS4', 174], ['OFF', 35], ['A4', 347], ['OFF', 69], ['G4', 694], ['OFF', 139], ['D5', 347], ['OFF', 69], ['F5', 694], ['OFF', 139], ['E5', 347], ['OFF', 69], ['DS5', 694], ['OFF', 139], ['B4', 347], ['OFF', 69], ['DS5', 347], ['OFF', 69], ['D5', 174], ['OFF', 35], ['CS5', 347], ['OFF', 69], ['CS4', 694], ['OFF', 139], ['B4', 347], ['OFF', 69], ['G4', 1389], ['OFF', 278], ['AS4', 347], ['OFF', 69], ['D5', 694], ['OFF', 139], ['AS4', 347], ['OFF', 69], ['D5', 694], ['OFF', 139], ['AS4', 347], ['OFF', 69], ['DS5', 694], ['OFF', 139], ['D5', 347], ['OFF', 69], ['CS5', 694], ['OFF', 139], ['A4', 347], ['OFF', 69], ['AS4', 347], ['OFF', 69], ['D5', 174], ['OFF', 35], ['CS5', 347], ['OFF', 69], ['CS4', 694], ['OFF', 139], ['D4', 347], ['OFF', 69], ['D5', 1389], ['OFF', 278], ['OFF', 347], ['OFF', 69], ['AS4', 347], ['OFF', 69], ['D5', 694], ['OFF', 139], ['AS4', 347], ['OFF', 69], ['D5', 694], ['OFF', 139], ['AS4', 347], ['OFF', 69], ['F5', 694], ['OFF', 139], ['E5', 347], ['OFF', 69], ['DS5', 694], ['OFF', 139], ['B4', 347], ['OFF', 69], ['DS5', 347], ['OFF', 69], ['D5', 174], ['OFF', 35], ['CS5', 347], ['OFF', 69], ['CS4', 694], ['OFF', 139], ['AS4', 347], ['OFF', 69], ['G4', 1389], ['OFF', 278]],
		}

	def time_ms(self):
		return int(time.monotonic() * 1000)

	def set(self, val):
		if val == True:
			self.buzzer.duty_cycle = 2**15
		else:
			self.buzzer.duty_cycle = 0

	def update_notes(self):
		if self.mld_playing: return
		if len(self.current_notes)>0:
			self.set(True)
			self.buzzer.frequency = tones[self.current_notes[0]]
		else:
			self.set(False)

	def press(self, *args, **kwargs):
		note = args[-1]
		self.current_notes.insert(0,note)
		self.update_notes()

	def rel(self, *args, **kwargs):
		note = args[-1]
		if note in self.current_notes:
			self.current_notes.remove(note)
		self.update_notes()

	def play(self, *args, **kwargs):
		if self.mld_playing:
			self.mld_playing = False
			self.set(False)
		else:
			self.play_melody(melody = self.melodies[args[-1]])

	def play_melody(self, melody=None, name=None):
		if melody == None and name != None:
			melody = self.melodies[name]
		# making a deep copy xD
		mld = []
		for note in melody:
			mld.append(note.copy())
		self.mld_duration = 0
		#upraveni mld [nota, od_kdy[ms]]
		next_start = 0
		for m in mld:
			dur = m[1]
			self.mld_duration += dur
			m[1] = next_start
			next_start += dur

		self.mld = mld
		self.mld_start = self.time_ms()
		self.mld_playing = True


		note = tones[mld[0][0]]
		if note != "OFF":
				self.set(True)
				self.buzzer.frequency = note
			else:
				self.set(False)

	def update_melody(self):
		position = self.time_ms() - self.mld_start
		if position>self.mld_duration:
			self.mld_playing = False
			self.set(False)
			return

		note = self.mld[0][0]
		for n in self.mld:
			if position > n[1]:
				note = n[0]
			else:
				break

		if note != self.mld_note:
			self.mld_note = note
			if note != "OFF":
				self.set(True)
				self.buzzer.frequency = tones[note]
			else:
				self.set(False)

	def on_runtime_enable(self, sandbox):
		return

	def on_runtime_disable(self, sandbox):
		return

	def during_bootup(self, sandbox):
		return

	def before_matrix_scan(self, sandbox):
		return

	def after_matrix_scan(self, sandbox):
		return

	def before_hid_send(self, sandbox):
		return

	def after_hid_send(self, sandbox):
		if self.mld_playing:
			self.update_melody()

	def on_powersave_enable(self, sandbox):
		return

	def on_powersave_disable(self, sandbox):
		return
