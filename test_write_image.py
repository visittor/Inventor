import cv2
import numpy as np
import sys
from graphic import *
from model import *
from get_config import *

class Bar1(Bar):
	def __init__(self,lookup):
		Bar.__init__(self,lookup,(314,5),30,300)
		pass
class Bar2(Bar):
	def __init__(self,lookup):
		Bar.__init__(self,lookup,(314,105),30,300)
		pass
class Bar3(Bar):
	def __init__(self,lookup):
		Bar.__init__(self,lookup,(314,205),30,300)
		pass

# class FoodQ(Food):
# 	def __init__(self):
# 		Food.__init__(self,"q",10,0,0,1000)
# class FoodW(Food):
# 	def __init__(self):
# 		Food.__init__(self,"w",0,10,0,1000)
# class FoodE(Food):
# 	def __init__(self):
# 		Food.__init__(self,"e",0,0,10,1000)

""" main here """
#############################################################################################################################################################################################
if __name__ == "__main__":
	img = cv2.imread("Template_draft1.png")
	dst =np.zeros((480,640,3),dtype = np.uint8)
	lookup = create_Gradient(img.shape)

	bar1 = Bar1(lookup)
	bar2 = Bar2(lookup)
	bar3 = Bar3(lookup)

	# foodq = FoodQ()
	# foodw = FoodW()
	# foode = FoodE()

	# body = Body("New",100,100,100,1000)
	# Food(protein = 1)
	foodStock = FoodStock()
	bodyStock = BodyStock()
	body = bodyStock.item

	while True:
		out = img

		bar1.create_bar(float(body.protein)/float(body.Adeprotein),out)
		bar2.create_bar(float(body.carb)/float(body.Adecarb),out)
		bar3.create_bar(float(body.fat)/float(body.Adefat),out)

		cv2.imshow('img',out)
		k = cv2.waitKey(1)
		if k not in range(256):
			food = None
		else:
			food = foodStock.findFromCode(chr(k))
		if food is not None:

			body.protein +=  food.protein
			body.carb += food.carb
			body.fat += food.fat
		if k == ord("b"):
			break
		# body.protein +=  food.protein
		# body.carb += food.carb
		# body.fat += food.fat
		# if k == ord("q"):
		# 	# print type(foodq.protein),foodq.protein,body.Adeprotein
		# 	body.protein +=  foodq.protein
		# 	body.carb += foodq.carb
		# 	body.fat += foodq.fat
		# elif k == ord("w"):
		# 	body.protein += foodw.protein 
		# 	body.carb += foodw.carb
		# 	body.fat += foodw.fat
		# 	body.energy += foodw.energy
		# elif k == ord("e"):
		# 	body.protein += foode.protein
		# 	body.carb += foode.carb
		# 	body.fat += foode.fat
		# 	body.energy += foode.energy
		# elif k == ord("b"):
		# 	break

	cv2.destroyAllWindows()
