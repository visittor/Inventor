from input import *
from model import *
from get_config import *
from G6reader import *
import threading 
import numpy as np
import cv2
from graphic import *

if __name__ == '__main__':
	Set_interrupt.add_attr('gender','m')
	Set_interrupt.add_attr('age','1')
	Set_interrupt.add_attr('bodyStock',BodyStock())
	Set_interrupt.add_attr('diseasStock',DiseasStock())
	Set_interrupt.add_attr('foodStock',FoodStock())
	Set_interrupt.add_attr('Doctor',DoctorStock().item)
	Set_interrupt.add_attr('RR',Read_RFID())
	emptyconfig = {'name':'empty_food','code':'empty_code',
						'protein':0,
						'carb':0,
						'fat':0,
						'energy':0,
						'vita':0,
						'vitd':0,
						'vite':0,
						'vitk':0,
						'vitc':0,
						'vitb':0,
						}
	Set_interrupt.add_attr('foodlist',[Food(**emptyconfig),Food(**emptyconfig),Food(**emptyconfig),Food(**emptyconfig),Food(**emptyconfig)])
	Set_interrupt.add_attr('bus',BusOut(18,16,12))

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
		#read rfid
		meal = make_meal(foodlist)
		body.eat(meal)

		diseas = cls.diseasStock.findFormCode('diseas'+body.report['lack_vit'][-1].lower())
		diseas.attack(body)

		cls.Doctor.diagnose(body)

		body.show_illness()

		body.get_bodyShape()

	class ReadRfid(threading.Thread):
		def __init__(self,cls,threadID):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.Klass = cls

		class _chip_select():
			def __init__(self,bus,value,lock):
				self._bus = bus
				self._value = value
				self.lock = lock
			def __enter__(self):
				self.lock.acquire()
				#print'Enter read card number',self._value
				self._bus.write(self._value)
				time.sleep(0.2)
		
			def __exit__(self,type,value,traceback):
				#print'Finish read card number',self._value
				#self._bus.write(6)
				time.sleep(0.1)
				self.lock.release()

		def run(self):
			print "rfid thread"
			self.Klass.lock.acquire()
			self.Klass.bus.write(1)
			self.Klass.RR.MIFAREReader.MFRC522_Init()
			self.Klass.bus.write(2)
			self.Klass.RR.MIFAREReader.MFRC522_Init()
			self.Klass.bus.write(3)
			self.Klass.RR.MIFAREReader.MFRC522_Init()
			self.Klass.bus.write(4)
			self.Klass.RR.MIFAREReader.MFRC522_Init()
			self.Klass.lock.release()
			time.sleep(0.1)
			while 1==1:
				count = 0
				with ReadRfid._chip_select(self.Klass.bus,0,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(1)
					print '1 ',uid
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						self.Klass.foodlist[count] = food
						count += 1
					#time.sleep(0.1)
				with ReadRfid._chip_select(self.Klass.bus,1,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(1)
					print '2 ',uid
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						self.Klass.foodlist[count] = food
						count += 1
					#time.sleep(0.1)
				with ReadRfid._chip_select(self.Klass.bus,2,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(1)
					print '3 ',uid
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						self.Klass.foodlist[count] = food
						count += 1
					#time.sleep(0.1)
				with ReadRfid._chip_select(self.Klass.bus,3,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(1)
					print '4 ',uid
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						self.Klass.foodlist[count] = food
						count += 1
					#time.sleep(0.1)
				with ReadRfid._chip_select(self.Klass.bus,4,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(1)
					print '5 ',uid
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						self.Klass.foodlist[count] = food
						count += 1
					#time.sleep(0.1)
				print "/////////////////"
			
	class ShowGraphic(threading.Thread):
		def __init__(self,cls,threadID):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.Klass = cls

		class _Bar1(Bar):
			def __init__(self,lookup):
				Bar.__init__(self,lookup,(314,5),30,300)
				pass
		class _Bar2(Bar):
			def __init__(self,lookup):
				Bar.__init__(self,lookup,(314,105),30,300)
				pass
		class _Bar3(Bar):
			def __init__(self,lookup):
				Bar.__init__(self,lookup,(314,205),30,300)
				pass
		class _Hexagon(Polygon):
			def __init__(self):
				Polygon.__init__(self,[740,170],[[671,31],[808,31],[878,170],[810,308],[669,308],[602,170]])

		def run(self):
			self.Klass.lock.acquire()
			img = cv2.imread("Template_draft1.png")
			# dst =np.zeros((480,640,3),dtype = np.uint8)
			lookup = create_Gradient(img.shape)
			self.Klass.lock.release()
			bar1 = _Bar1(lookup)
			bar2 = _Bar2(lookup)
			bar3 = _Bar3(lookup)
			hexa = _Hexagon()
			try:
				while True:
					out = img.copy()

					food = make_meal(self.Klass.foodlist)
					percenVit = [[food.vitA,food.vitA],
								[food.vitD,food.vitD],
								[food.vitE,food.vitE],
								[food.vitK,food.vitK],
								[food.vitC,food.vitC],
								[food.vitB,food.vitB],]

					hexa.create_Polygon(percenVit,out)
					bar1.create_bar(food.protein,out)
					bar2.create_bar(body.card,out)
					bar3.create_bar(body.fat,out)

					cv2.imshow('img',out)
					k = cv2.waitKey(1)

				cv2.destroyAllWindows()
			except KeyboardInterrupt:
				cv2.destroyAllWindows()
			finally:
				cv2.destroyAllWindows()

	Set_interrupt.add_thread(ReadRfid)
	Set_interrupt.run()
