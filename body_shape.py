import RPi.GPIO as GPIO
from graphic import Sound,Non_thr_sond
def body_shape(report):
	if report["energy"] > 1.2:
		GPIO.output(7,1)
		Non_thr_sond("Sound/Fat.mp3")
	elif report["energy"] < 0.8:
		GPIO.output(7,0)
		Non_thr_sond("Sound/Thin.mp3")
	else:
		GPIO.output(7,0)

