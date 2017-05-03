import RPi.GPIO as GPIO
from input import Set_interrupt

def body_shape(report):
	if report["energy"] > 1.2:
		Set_interrupt.play_list.append(["Sound/why_im_fat.mp3",3])
		print "I'm fat"
		GPIO.output(7,0)
	elif report["energy"] < 0.8:
		Set_interrupt.play_list.append(["Sound/im_weak.mp3",3])
		print "I'm thin"
		GPIO.output(7,1)
	else:
		Set_interrupt.play_list.append(["Sound/food_ok.mp3",3])
		GPIO.output(7,1)
