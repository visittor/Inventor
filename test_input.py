from input import *
import RPI.GPIO as GPIO

if __name__ == '__main__':
	try:
		Set_interrupt.add_attr('gender','m')
		Set_interrupt.add_attr('age','1')

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
			print "age = ",cls.age
			print "gender = ",cls.gender

		while 1==1:
			continue
	except:
		GPIO.cleanup()
	finally:
		GPIO.cleanup()
