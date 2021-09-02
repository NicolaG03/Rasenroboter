import time
import board
import adafruit_tca9548a
from smbus import SMBus


_REGISTER_SHIFT_BIT = 0x35
_REGISTER_DISTANCE = 0x5e

class GP2Y0E03:
	def __init__(self, i2c):
		self.i2c = i2c

	def _address(self, address):
		self.address = address

	def _register8(self, register, value=None):
		return self.i2c.read_byte_data(self.address, register)

	def _register16(self, register, value=None):
		return self.i2c.read_i2c_block_data(self.address, register,2)

	def read(self, raw=False):
		shift = self._register8(_REGISTER_SHIFT_BIT)
		time.sleep(0.1)
		value = self._register16(_REGISTER_DISTANCE)
		dist = (((value[0] << 4) | value[1])/16)/2**shift # Distance in cm - see http://media.digikey.com/pdf/Data%20Sheets/Sharp%20PDFs/GP2Y0E03_Spec_Feb2013.pdf
		return dist
def auslesen ():
	v_error = 1
	v_text = 1000.01
	while (v_text == 1000.01):
		while v_error:
			# Create I2C bus as normal
			i2c = board.I2C()  # uses board.SCL and board.SDA
			# Create the TCA9548A object and give it the I2C bus
			tca = adafruit_tca9548a.TCA9548A(i2c)
			i2c = SMBus(1)
			s = GP2Y0E03(i2c)
			s._address(0x40)
			try:
				if tca[0].try_lock():
					time.sleep(0.1)
					print ("Sensor0")
					#print (s.read())
					v_text = s.read()
					tca[0].unlock()
					v_error = 0
			except OSError:
				break
	print (v_text)
