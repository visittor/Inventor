import RPi.GPIO as GPIO
from input import Set_interrupt

def body_shape(report):
	if report["energy"] > 1.2:
		Set_interrupt.play_list.append("Sound/Fat.mp3")
		GPIO.output(7,1)
	elif report["energy"] < 0.8:
		Set_interrupt.play_list.append("Sound/Thin.mp3")
		GPIO.output(7,0)
	else:
		GPIO.output(7,0)
