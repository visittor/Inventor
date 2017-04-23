import RPi.GPIO as GPIO

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
	# class _interrupt_obj(obj):
	def __init__(self,port,event):
		self.port = port
		self.event = event

	def __call__(self,func):
		try:
			GPIO.setup(self.port,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
		except:
			print "something wrong file input.py line something"
		GPIO.add_event_detect(self.port,self.event,callback = lambda x: func(self.__class__),bouncetime = 200)

	@classmethod
	def add_attr(cls,name,value):
		setattr(cls,name,value)

	@classmethod
	def add_thread(cls,thread_):
		threads.append(thread_(cls,len(threads)))

	@classmethod
	def run(cls):
		for i in threads:
			i.start()





		
