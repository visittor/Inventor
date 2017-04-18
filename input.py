import RPI.GPIO as GPIO

class BusIn(object):
	def __init__(self,*args):
		self._bus = args
		for port in self._bus:
			GPIO.setup(port,GPIO.IN)

	def read(self):
		mask = 1
		value = 0
		for port in self._bus:
			value += PIO.input(port)*mask
			mask *= 2
		return value

class BusOut(object):
	def __init__(self,*args):
		self._bus = args
		for port in self._bus:
			GPIO.setup(port,GPIO.OUT)

	def write(self,value):
		mask = 1
		for port in self._bus:
			GPIO.output(port,value&mask)
			mask *= 2

class Set_Interrupt(BusIn):
	def __init__(self,):