from input import *
from model import *
from get_config import *
from G6reader import *
import threading 
import numpy as np
import cv2
from graphic import *
import RPi.GPIO as GPIO
import pygame
import subprocess
if __name__ == '__main__':
	Set_interrupt.add_attr('gender','m')
	Set_interrupt.add_attr('age','1')
	Set_interrupt.add_attr('bodyStock',BodyStock())
	Set_interrupt.add_attr('body',Set_interrupt.bodyStock.findFromCode('m1')[0])
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
	Set_interrupt.add_attr('emptyconfig',emptyconfig)
	Set_interrupt.add_attr('foodlist',[Food(**emptyconfig),Food(**emptyconfig),Food(**emptyconfig),Food(**emptyconfig),Food(**emptyconfig)])
	Set_interrupt.add_attr('bus',BusOut(18,16,12))
	Set_interrupt.add_attr('interrupt_Lock',1)
	Set_interrupt.add_attr('play_list',[])

	Set_interrupt.add_attr('gender_age_flag',{"age":1,"gender":1})
	GPIO.setup(7,GPIO.OUT)
	GPIO.output(7,1)
	@Set_interrupt(29,GPIO.FALLING)
	def male_select(cls):
		if Set_interrupt.interrupt_Lock == 1:
			cls.gender = 'm'
			cls.body = cls.bodyStock.findFromCode(cls.gender+cls.age)[0]
			cls.gender_age_flag["gender"] = 0
			if cls.gender_age_flag["age"]:
				cls.play_list.append(["Sound/choose_age.mp3",2])
			else:
				cls.play_list.append(["Sound/choose_card.mp3",4])
			print cls.body
			print "choose male"

	@Set_interrupt(31,GPIO.FALLING)
	def female_select(cls):
		if Set_interrupt.interrupt_Lock == 1:
			cls.gender = 'f'
			cls.body = cls.bodyStock.findFromCode(cls.gender+cls.age)[0]
			cls.gender_age_flag["gender"] = 0
			if cls.gender_age_flag["age"]:
				cls.play_list.append(["Sound/choose_age.mp3",2])
			else:
				cls.play_list.append(["Sound/choose_card.mp3",4])
			print cls.body
			print "choose female"

	@Set_interrupt(33,GPIO.FALLING)
	def age1_select(cls):
		if Set_interrupt.interrupt_Lock == 1:
			cls.age = '1'
			cls.body = cls.bodyStock.findFromCode(cls.gender+cls.age)[0]
			cls.gender_age_flag["age"] = 0
			if cls.gender_age_flag["gender"]:
				cls.play_list.append(["Sound/choose_gender.mp3",2])
			else:
				cls.play_list.append(["Sound/choose_card.mp3",4])
			print cls.body
			print "choose 1st age"
		#player = subprocess.Popen(["mplayer","Sound/Vit_K.mp3"],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
	@Set_interrupt(35,GPIO.FALLING)
	def age2_select(cls):
		if Set_interrupt.interrupt_Lock == 1:
			cls.age = '2'
			cls.body = cls.bodyStock.findFromCode(cls.gender+cls.age)[0]
			cls.gender_age_flag["age"] = 0
			if cls.gender_age_flag["gender"]:
				cls.play_list.append(["Sound/choose_gender.mp3",2])
			else:
				cls.play_list.append(["Sound/choose_card.mp3",4])
			print cls.body
			print "choose 2nd age"

	@Set_interrupt(37,GPIO.FALLING)
	def age3_select(cls):
		if Set_interrupt.interrupt_Lock == 1:
			cls.age = '3'
			cls.body = cls.bodyStock.findFromCode(cls.gender+cls.age)[0]
			cls.gender_age_flag["age"] = 0
			if cls.gender_age_flag["gender"]:
				cls.play_list.append(["Sound/choose_gender.mp3",2])
			else:
				cls.play_list.append(["Sound/choose_card.mp3",4])
			cls.gender_time_choose = time.time()
			print cls.body
			print "choose 3th age"

	@Set_interrupt(32,GPIO.FALLING)
	def eat_select(cls):
		#read rfid
		print "Enter ..."
		if Set_interrupt.interrupt_Lock == 1:
			GPIO.remove_event_detect(29)
			GPIO.remove_event_detect(31)
			GPIO.remove_event_detect(33)
			GPIO.remove_event_detect(35)
			GPIO.remove_event_detect(37)
			cls.gender_age_flag["age"] = 1
			cls.gender_age_flag["gender"] = 1

			meal = make_meal(cls.foodlist)
			cls.body.eat(meal)
			print "Eat!!!!"
			# diseas = cls.diseasStock.findFromCode('diseas'+cls.body.report['lack_vit'][-1].lower())[0]
			# diseas.attack(cls.body)

			# cls.Doctor.diagnose(cls.body)
			# cls.body.show_illness()
			cls.body.get_bodyShape()
			GPIO.add_event_detect(29,GPIO.FALLING,callback = lambda x: male_select(Set_interrupt),bouncetime = 1000)
			GPIO.add_event_detect(31,GPIO.FALLING,callback = lambda x: female_select(Set_interrupt),bouncetime = 1000)
			GPIO.add_event_detect(33,GPIO.FALLING,callback = lambda x: age1_select(Set_interrupt),bouncetime = 1000)
			GPIO.add_event_detect(35,GPIO.FALLING,callback = lambda x: age2_select(Set_interrupt),bouncetime = 1000)
			GPIO.add_event_detect(37,GPIO.FALLING,callback = lambda x: age3_select(Set_interrupt),bouncetime = 1000)
		else:
			print "in else:"

		print "Exit..."	

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
				self._bus.write(self._value)
		
			def __exit__(self,type,value,traceback):
				self.lock.release()
				time.sleep(0.1)

		def run(self):
			print "Enter rfid thread"
			self.Klass.lock.acquire()
			self.Klass.bus.write(0)
			self.Klass.RR.MIFAREReader.MFRC522_Init()
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
			self.Klass.e.wait()
			while self.Klass.e.is_set():
				count = 0
				with ReadRfid._chip_select(self.Klass.bus,0,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(0.5)
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						if len(food)>0:
							self.Klass.foodlist[count] = food[0]
						else:
							self.Klass.foodlist[count] = None
						count += 1
					else:
						self.Klass.foodlist[count] = None
						count += 1
				with ReadRfid._chip_select(self.Klass.bus,1,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(0.5)
					# print '2 ',uid
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						if len(food)>0:
							self.Klass.foodlist[count] = food[0]
						else:
							self.Klass.foodlist[count] = None
						count += 1
					else:
						self.Klass.foodlist[count] = None
						count += 1
					#time.sleep(0.1)
				with ReadRfid._chip_select(self.Klass.bus,2,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(0.5)
					# print '3 ',uid
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						if len(food)>0:
							self.Klass.foodlist[count] = food[0]
						else:
							self.Klass.foodlist[count] = None
						count += 1
					else:
						self.Klass.foodlist[count] = None
						count += 1
				with ReadRfid._chip_select(self.Klass.bus,3,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(0.5)
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						if len(food)>0:
							self.Klass.foodlist[count] = food[0]
						else:
							self.Klass.foodlist[count] = None
						count += 1
					else:
						self.Klass.foodlist[count] = None
						count += 1
				with ReadRfid._chip_select(self.Klass.bus,4,self.Klass.lock) as cs:
					uid = self.Klass.RR.get_uid(0.5)
					if len(uid)>0:
						food = self.Klass.foodStock.findFromCode(str(uid))
						if len(food)>0:
							self.Klass.foodlist[count] = food[0]
						else:
							self.Klass.foodlist[count] = None
						count += 1
					else:
						self.Klass.foodlist[count] = None
						count += 1
			print "Exit rfid thread"
			
	class ShowGraphic(threading.Thread):
		def __init__(self,cls,threadID):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.Klass = cls
		
		class _Bar1(Bar):
			def __init__(self,lookup):
				# Bar.__init__(self,lookup,(314,5),30,300)
				Bar.__init__(self,lookup,(846,107),98,365)
				pass
		class _Bar2(Bar):
			def __init__(self,lookup):
				# Bar.__init__(self,lookup,(314,105),30,300)
				Bar.__init__(self,lookup,(846,267),98,365)
				pass
		class _Bar3(Bar):
			def __init__(self,lookup):
				# Bar.__init__(self,lookup,(314,205),30,300)
				Bar.__init__(self,lookup,(846,427),98,365)
				pass
		class _Hexagon(Polygon):
			def __init__(self):
				Polygon.__init__(self,[1357,700],[[1357,594],[1458,666],[1420,785],[1294,787],[1257,666]])
		class _En_Bar(Energy_Bar):
			def __init__(self,lookup):
				Energy_Bar.__init__(self,lookup,(846,750),250,387)
		class _Header_Text(object):
			def __init__(self):
				self.font = cv2.FONT_HERSHEY_SIMPLEX
				self.dict_text = {"m":"Boy","f":"Girl","1":"0-6","2":"6-10","3":">10"}
			def create_text(self,gender,age,out):
				cv2.putText(out,self.dict_text[gender]+"     age:     "+self.dict_text[age]+" years old",(200,200), self.font, 1,(0,0,0),1,cv2.LINE_AA)

		def run(self):
			print "Enter graphic thread"
			self.Klass.lock.acquire()
			img = cv2.imread("Template_draft2.png")
			# dst =np.zeros((480,640,3),dtype = np.uint8)
			# lookup = create_Gradient(img.shape)
			lookup = cv2.imread("gradient_PCF.png")
			self.Klass.lock.release()
			bar1 = ShowGraphic._Bar1(lookup)
			bar2 = ShowGraphic._Bar2(lookup)
			bar3 = ShowGraphic._Bar3(lookup)
			hexa = ShowGraphic._Hexagon()
			en_bar = ShowGraphic._En_Bar(lookup)
			header_text = ShowGraphic._Header_Text()

			try:
				self.Klass.e.wait()
				while self.Klass.e.is_set():
					out = img.copy()

					food = make_meal(self.Klass.foodlist)
					#print "I am here",food.protein
					self.Klass.lock.acquire()
					header_text.create_text(self.Klass.gender,self.Klass.age,out)

					percenVit = [[food.vitA/self.Klass.body.AdevitA,food.vitA/self.Klass.body.AdevitA],
								[food.vitE/self.Klass.body.AdevitE,food.vitE/self.Klass.body.AdevitE],
								[food.vitK/self.Klass.body.AdevitK,food.vitK/self.Klass.body.AdevitK],
								[food.vitC/self.Klass.body.AdevitC,food.vitC/self.Klass.body.AdevitC],
								[food.vitB/self.Klass.body.AdevitB,food.vitB/self.Klass.body.AdevitB],]

					hexa.create_Polygon(percenVit,out)
					bar1.create_bar(food.protein/self.Klass.body.Adeprotein,out)
					bar2.create_bar(food.carb/self.Klass.body.Adecarb,out)
					bar3.create_bar(food.fat/self.Klass.body.Adefat,out)
					en_bar.create_energy_bar(food.energy/self.Klass.body.Adeenergy,out)

					'''percenVit = [[self.Klass.body.report["vitA"],self.Klass.body.report["vitA"]],
								[self.Klass.body.report["vitD"],self.Klass.body.report["vitD"]],
								[self.Klass.body.report["vitE"],self.Klass.body.report["vitE"]],
								[self.Klass.body.report["vitK"],self.Klass.body.report["vitK"]],
								[self.Klass.body.report["vitC"],self.Klass.body.report["vitC"]],
								[self.Klass.body.report["vitB"],self.Klass.body.report["vitB"]],]

					hexa.create_Polygon(percenVit,out)
					bar1.create_bar(self.Klass.body.report["protein"],out)
					bar2.create_bar(self.Klass.body.report["carb"],out)
					bar3.create_bar(self.Klass.body.report["fat"],out)
					en_bar.create_energy_bar(self.Klass.body.report["energy"],out)'''

					cv2.imshow('img',out)
					self.Klass.lock.release()
					k = cv2.waitKey(1)

				cv2.destroyAllWindows()
				print "Exit graphic thread"
			except KeyboardInterrupt:
				cv2.destroyAllWindows()
				print "Exit graphic thread"
			finally:
				cv2.destroyAllWindows()
	class Sound_quene(threading.Thread):
		def __init__(self,cls,threadID):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.Klass = cls

		def run(self):
			print "Enter Sound_quene"
			self.Klass.e.wait()
			while self.Klass.e.is_set():
				if len(self.Klass.play_list) > 0:
					Set_interrupt.interrupt_Lock = 0
					Non_thr_sond(self.Klass.play_list[0][0],time_play = self.Klass.play_list[0][1])
					self.Klass.play_list.pop(0)
					Set_interrupt.interrupt_Lock = 1
				time.sleep(0.1)
			print "Exit Sound_quene"

	Set_interrupt.add_thread(ReadRfid)
	Set_interrupt.add_thread(ShowGraphic)
	Set_interrupt.add_thread(Sound_quene)
	Set_interrupt.run()
