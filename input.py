import RPi.GPIO as GPIO
import threading
class BusIn(object):
	def __init__(self,*args):
		self._bus = args
		for port in self._bus:
			GPIO.setup(port,GPIO.IN)

	def read(self):
		mask = 1
		value = 0
		for port in self._bus:
			value += GPIO.input(port)*mask
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

class Set_interrupt(object):
	threads = []
	lock = threading.Lock()
	e = threading.Event()
	# class _interrupt_obj(obj):
	def __init__(self,port,event):
		self.port = port
		self.event = event
		

	def __call__(self,func):
		try:
			# GPIO.setup(self.port,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
			GPIO.setup(self.port,GPIO.IN)
		except:
			print "something wrong file input.py line something"
		GPIO.add_event_detect(self.port,self.event,callback = lambda x: func(self.__class__),bouncetime = 500)

	@classmethod
	def add_attr(cls,name,value):
		setattr(cls,name,value)

	@classmethod
	def add_thread(cls,thread_):
		print cls 
		cls.threads.append(thread_(cls,len(cls.threads)))

	@classmethod
	def run(cls):
		for i in cls.threads:
			i.start()
		cls.e.set()
		while 1 == 1:
			k = raw_input("k to kill program: ")
			if k == 'k':
				cls.e.clear()
				break

		for i in cls.threads:
			i.join()
		GPIO.cleanup()





		
