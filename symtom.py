from graphic import Sound,Non_thr_sond
def symtomA(inhibitor):
	if inhibitor['vitA'] < 0.5:
		print "I'm lack of vitamin A"
	return "vitA"

def symtomD(inhibitor):
	if inhibitor['vitD'] < 0.5:
		print "I'm lack of vitamin D"
	return "vitD"

def symtomE(inhibitor):
	if inhibitor['vitE'] < 0.5:
		print "I'm lack of vitamin E"
	return "vitE"

def symtomK(inhibitor):
	if inhibitor['vitK'] < 0.5:
		Non_thr_sond("Sound/Vit_K.mp3")
		print "I'm lack of vitamin K"
	return "vitK"

def symtomC(inhibitor):
	if inhibitor['vitC'] < 0.5:
		print "I'm lack of vitamin C"
	return "vitC"

def symtomB(inhibitor):
	if inhibitor['vitB'] < 0.5:
		print "I'm lack of vitamin B"
	return "vitB"
