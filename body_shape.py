import RPi.GPIO as GPIO
from graphic import Non_thr_sond
from input import Set_interrupt

def body_shape(report):
	if report["energy"] > 1.2:
		Set_interrupt.lock.acquire()
		GPIO.output(7,1)
		Set_interrupt.track_name.append("Sound/Fat.mp3")
		Set_interrupt.lock.release()
	elif report["energy"] < 0.8:
		Set_interrupt.lock.acquire()
		GPIO.output(7,0)
		Set_interrupt.track_name.append("Sound/Thin.mp3")
		Set_interrupt.lock.release()
	else:
		GPIO.output(7,0)

