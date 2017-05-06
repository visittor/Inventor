import RPi.GPIO as GPIO
from input import Set_interrupt

def body_shape(report):
	if report[report["lack_vit"]] < 0.5:
		Set_interrupt.play_list.append(["Sound/im_not_ok.mp3",2])
		Set_interrupt.play_list.append(["Sound/lack_"+report["lack_vit"][-1].lower()+".mp3",3])

	if report["energy"] > 1.2:
		Set_interrupt.play_list.append(["Sound/why_im_fat.mp3",3])
		print "I'm fat"
		GPIO.output(7,0)
	elif report["energy"] < 0.8:
		Set_interrupt.play_list.append(["Sound/im_weak.mp3",3])
		print "I'm thin"
		GPIO.output(7,1)
	elif report[report["'lack_vit'"]]>1:
		Set_interrupt.play_list.append(["Sound/food_ok.mp3",3])
		GPIO.output(7,1)
