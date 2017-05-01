import RPi.GPIO as GPIO
from graphic import Non_thr_sond
from input import Set_interrupt

def body_shape(report):
	if report["energy"] > 1.2:
		GPIO.output(7,1)
		Set_interrupt.track_name = "Sound/Fat.mp3"
	elif report["energy"] < 0.8:
		GPIO.output(7,0)
		Set_interrupt.track_name = "Sound/Thin.mp3"
	else:
		GPIO.output(7,0)

