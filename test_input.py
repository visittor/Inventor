from input import *
import RPi.GPIO as GPIO
import sys

if __name__ == '__main__':
	try:
		GPIO.setmode(GPIO.BOARD)
		Set_interrupt.add_attr('gender','m')
		Set_interrupt.add_attr('age','1')

		@Set_interrupt(29,GPIO.RISING)
		def male_select(cls):
			cls.gender = 'm'	
			print "RISING male"
		@Set_interrupt(31,GPIO.RISING)
		def female_select(cls):
			cls.gender = 'f'
			print "RISING female"
		@Set_interrupt(33,GPIO.RISING)
		def age1_select(cls):
			cls.age = '1'
			print "RISING age1"
		@Set_interrupt(35,GPIO.RISING)
		def age2_select(cls):
			cls.age = '2'
			print "RISING age 2"

		@Set_interrupt(37,GPIO.RISING)
		def age3_select(cls):
			cls.age = '3'
			print "RISING age3"
		@Set_interrupt(32,GPIO.RISING)
		def eat_select(cls):
			print "\nage = ",cls.age
			print "gender = ",cls.gender,"\n"

		#GPIO.setmode(GPIO.BOARD)
		#GPIO.setup(33,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
		while 1==1:
			#print GPIO.input(33)
			pass	
			
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit(1)
	finally:
		GPIO.cleanup()
		sys.exit(0)
