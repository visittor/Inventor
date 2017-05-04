
import cv2
import numpy as np
import sys
from graphic import *
# from model import *
# from get_config import *
# from Doctor import *

# class Bar1(Bar):
# 	def __init__(self,lookup):
# 		Bar.__init__(self,lookup,(314,5),30,300)
# 		pass
# class Bar2(Bar):
# 	def __init__(self,lookup):
# 		Bar.__init__(self,lookup,(314,105),30,300)
# 		pass
# class Bar3(Bar):
# 	def __init__(self,lookup):
# 		Bar.__init__(self,lookup,(314,205),30,300)
# 		pass
# class Hexagon(Polygon):
# 	def __init__(self):
# 		Polygon.__init__(self,[740,170],[[671,31],[808,31],[878,170],[810,308],[669,308],[602,170]])
class Bar1(Bar):
	def __init__(self,lookup):
		# Bar.__init__(self,lookup,(314,5),30,300)
		Bar.__init__(self,lookup,(846,107),98,365)
		pass
class Bar2(Bar):
	def __init__(self,lookup):
		# Bar.__init__(self,lookup,(314,105),30,300)
		Bar.__init__(self,lookup,(846,267),98,365)
		pass
class Bar3(Bar):
	def __init__(self,lookup):
		# Bar.__init__(self,lookup,(314,205),30,300)
		Bar.__init__(self,lookup,(846,427),98,365)
		pass
class Hexagon(Polygon):
	def __init__(self):
		Polygon.__init__(self,[1357,700],[[1357,594],[1458,666],[1420,785],[1294,787	],[1257,666]])
class En_Bar(Energy_Bar):
	def __init__(self,lookup):
		Energy_Bar.__init__(self,lookup,(846,750),250,387)
"""main here(test)"""
#############################################################################################################################################################################################
if __name__ == "__main__":
	img = cv2.imread("Template_draft2.png")
	lookup = cv2.imread("gradient_PCF.png")
	# dst =np.zeros((480,640,3),dtype = np.uint8)
	# lookup = create_Gradient(img.shape)

	cv2.namedWindow('img')
	cv2.setMouseCallback('img',mouse_callback)

	bar1 = Bar1(lookup)
	bar2 = Bar2(lookup)
	bar3 = Bar3(lookup)
	hexa = Hexagon()
	en_bar = En_Bar(lookup)


	# foodStock = FoodStock()
	# bodyStock = BodyStock()
	# diseasStock = DiseasStock()
	# Doctor = DoctorStock().item
	# body = bodyStock.item

	while True:
		out = img.copy()

		percenVit = [[1,1],
					 [1,1],
					 [1,1],
					 [1,1],
					 [1,1],]
		hexa.create_Polygon(percenVit,out)
		bar1.create_bar(0,out)
		bar2.create_bar(1.5,out)
		bar3.create_bar(1.5,out)
		mask = en_bar.create_energy_bar(1.5,out)

		cv2.imshow('img',out)
		k = cv2.waitKey(1)

		# if k not in range(255):
		# 	food = None
		# else:
			
		# 	food = foodStock.findFromCode(chr(k))
		# if  food is not None and len(food)>0:
		# 	print food
		# 	body.eat(food[0])
		# 	# print body.report
		# 	# body.protein +=  food.protein
		# 	# body.carb += food.carb
		# 	# body.fat += food.fat
		if k == ord("b"):
			break

	cv2.destroyAllWindows()
