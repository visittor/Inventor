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
class Hexagon(Polygon):
	def __init__(self):
		Polygon.__init__(self,[740,170],[[671,31],[808,31],[878,170],[810,308],[669,308],[602,170]])
"""main here"""
#############################################################################################################################################################################################
if __name__ == "__main__":
	img = cv2.imread("Template_draft1.png")
	# dst =np.zeros((480,640,3),dtype = np.uint8)
	lookup = create_Gradient(img.shape)

	cv2.namedWindow('img')
	cv2.setMouseCallback('img',mouse_callback)

	bar1 = Bar1(lookup)
	bar2 = Bar2(lookup)
	bar3 = Bar3(lookup)
	hexa = Hexagon()
	# hexa = Polygon((300,305),)

	foodStock = FoodStock()
	bodyStock = BodyStock()
	body = bodyStock.item

	while True:
		out = img

		percenVit = [[float(body.vitA)/float(body.AdevitA)],
					 [float(body.vitD)/float(body.AdevitD)],
					 [float(body.vitE)/float(body.AdevitE)],
					 [float(body.vitK)/float(body.AdevitK)],
					 [float(body.vitC)/float(body.AdevitC)],
					 [float(body.vitB)/float(body.AdevitB)],]
		hexa.create_Polygon(percenVit,out)
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
			body.eat(food)
			# body.protein +=  food.protein
			# body.carb += food.carb
			# body.fat += food.fat
		if k == ord("b"):
			break

	cv2.destroyAllWindows()
