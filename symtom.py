from graphic import Sound,Non_thr_sond
from input import Set_interrupt
def symtomA(inhibitor):
	if inhibitor['vitA'] < 0.5:
		Set_interrupt.play_list.append(["Sound/im_not_ok.mp3",2])
		Set_interrupt.play_list.append(["Sound/lack_a.mp3",3])
		print "I'm lack of vitamin A"
	return "vitA"

def symtomD(inhibitor):
	if inhibitor['vitD'] < 0.5:
		Set_interrupt.play_list.append(["Sound/im_not_ok.mp3",2])
		Set_interrupt.play_list.append(["Sound/lack_d.mp3",3])
		print "I'm lack of vitamin D"
	return "vitD"

def symtomE(inhibitor):
	if inhibitor['vitE'] < 0.5:
		Set_interrupt.play_list.append(["Sound/im_not_ok.mp3",2])
		Set_interrupt.play_list.append(["Sound/lack_e.mp3",3])
		print "I'm lack of vitamin E"
	return "vitE"

def symtomK(inhibitor):
	if inhibitor['vitK'] < 0.5:
		Set_interrupt.play_list.append(["Sound/im_not_ok.mp3",2])
		Set_interrupt.play_list.append(["Sound/lack_k.mp3",3])
		print "I'm lack of vitamin K"
	return "vitK"

def symtomC(inhibitor):
	if inhibitor['vitC'] < 0.5:
		Set_interrupt.play_list.append(["Sound/im_not_ok.mp3",2])
		Set_interrupt.play_list.append(["Sound/lack_c.mp3",3])
		print "I'm lack of vitamin C"
	return "vitC"

def symtomB(inhibitor):
	if inhibitor['vitB'] < 0.5:
		Set_interrupt.play_list.append(["Sound/im_not_ok.mp3",2])
		Set_interrupt.play_list.append(["Sound/lack_b6.mp3",3])
		print "I'm lack of vitamin B"
	return "vitB"
