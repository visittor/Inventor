from graphic import Non_thr_sond
from input import Set_interrupt
def symtomA(inhibitor):
	if inhibitor['vitA'] < 0.5:
		Set_interrupt.eat_Lock = 0
		Set_interrupt.track_name.append("Sound/Vit_A.mp3")
		print "I'm lack of vitamin A"
		Set_interrupt.eat_Lock = 1
	return "vitA"

def symtomD(inhibitor):
	if inhibitor['vitD'] < 0.5:
		Set_interrupt.eat_Lock = 0
		Set_interrupt.track_name.append("Sound/Vit_D.mp3") 
		print "I'm lack of vitamin D"
		Set_interrupt.eat_Lock = 1
	return "vitD"

def symtomE(inhibitor):
	if inhibitor['vitE'] < 0.5:
		Set_interrupt.eat_Lock = 0
		Set_interrupt.track_name.append("Sound/Vit_E.mp3")
		print "I'm lack of vitamin E"
		Set_interrupt.eat_Lock = 1
	return "vitE"

def symtomK(inhibitor):
	if inhibitor['vitK'] < 0.5:
		Set_interrupt.eat_Lock = 0
		Set_interrupt.track_name.append("Sound/Vit_K.mp3")
		# thr = Sound("Sound/Vit_K.mp3")
		# thr.start()
		print "I'm lack of vitamin K"
		Set_interrupt.eat_Lock = 1
	return "vitK"

def symtomC(inhibitor):
	if inhibitor['vitC'] < 0.5:
		Set_interrupt.eat_Lock = 0
		Set_interrupt.track_name.append("Sound/Vit_C.mp3")
		print "I'm lack of vitamin C"
		Set_interrupt.eat_Lock = 1
	return "vitC"

def symtomB(inhibitor):
	if inhibitor['vitB'] < 0.5:
		Set_interrupt.eat_Lock = 0
		Set_interrupt.track_name.append("Sound/Vit_B.mp3")
		print "I'm lack of vitamin B"
		Set_interrupt.eat_Lock = 1
	return "vitB"
