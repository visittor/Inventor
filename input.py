import RPI.GPIO as GPIO
from model import *
from get_config import *

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
	
	# class _interrupt_obj(obj):
	def __init__(self,port,event):
		self.port = port
		self.event = event

	def __call__(self,func):
		try:
			GPIO.setup(self.port,GPIO.IN)
		except:
			print "something wrong file input.py line something"
		GPIO.add_event_detect(self.port,self.event,callback = lambda x: func(self.__class__))

	def add_attr(self,name,value):
		setattr(self.__class__,name,value)
"""
Set_interrupt.add_attr('gender','m')
Set_interrupt.add_attr('age','1')
Set_interrupt.add_attr('bodyStock',BodyStock())
Set_interrupt.add_attr('diseasStock',DiseasStock())
Set_interrupt.add_attr('foodStock',FoodStock())
Set_interrupt.add_attr('Doctor',DoctorStock().item)

@Set_interrupt(29,GPIO.RISING)
def male_select(cls):
	cls.gender = 'm'

@Set_interrupt(31,GPIO.RISING)
def female_select(cls):
	cls.gender = 'f'

@Set_interrupt(33,GPIO.RISING)
def age1_select(cls):
	cls.age = '1'

@Set_interrupt(35,GPIO.RISING)
def age2_select(cls):
	cls.age = '2'

@Set_interrupt(37,GPIO.RISING)
def age3_select(cls):
	cls.age = '3'

@Set_interrupt(32,GPIO.RISING)
def eat_select(cls):
	body = cls.bodyStock.findFormCode(cls.gender+cls.age)
	 """ """read rfid""""""
	meal = make_meal(foodlist)
	body.eat(meal)

	diseas = cls.diseasStock.findFormCode('diseas'+body.report['lack_vit'][-1].lower())
	diseas.attack(body)

	cls.Doctor.diagnose(body)

	body.show_illness()

	body.get_bodyShape()
"""





		